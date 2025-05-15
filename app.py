import streamlit as st
import os
import fitz  # PyMuPDF
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# Setup
st.set_page_config(page_title="AI Assistant: Kazakhstan Constitution")
st.title("🇰🇿 AI Assistant on Kazakhstan Constitution")

# Initialize vector store
CHROMA_DIR = "chroma_db"
os.makedirs(CHROMA_DIR, exist_ok=True)

# Embedding and vector store setup
embedding = OllamaEmbeddings(model="mistral")
vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embedding)

# File upload
uploaded_files = st.file_uploader("Upload document(s)", type=["pdf"], accept_multiple_files=True)

# Function to extract text from PDFs
def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Process uploaded files
if uploaded_files:
    st.success("Documents uploaded successfully!")
    for file in uploaded_files:
        raw_text = extract_text_from_pdf(file)
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = splitter.split_text(raw_text)
        documents = [Document(page_content=t) for t in texts]
        vectorstore.add_documents(documents)
        vectorstore.persist()

# Chat functionality
query = st.text_input("Ask a question about the Constitution or uploaded documents")

if query:
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOllama(model="mistral", temperature=0),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    response = qa_chain({"query": query})
    st.write("### Answer:")
    st.write(response["result"])
