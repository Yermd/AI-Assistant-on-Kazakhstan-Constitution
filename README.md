# 🇰🇿 AI Assistant on Constitution of Kazakhstan

This project is a **local AI assistant** that can answer questions based on uploaded PDF documents, especially the Constitution of the Republic of Kazakhstan. It runs offline using [Ollama](https://ollama.com/) and models like `mistral`.

---

## 📸 Demo

![demo screenshot](screenshots/demo.png) <!-- You can replace this with your own screenshot later -->

---

## 🚀 Features

✅ Upload one or multiple PDF files  
✅ Automatically parse and store the document content  
✅ Ask natural-language questions about the documents  
✅ Runs **100% locally** using Ollama and LangChain  
✅ Streamlit-based UI  

---

## 🧰 Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama (`mistral`, `gemma`, etc.)
- PyMuPDF (text extraction from PDF)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-constitution-assistant.git
cd ai-constitution-assistant
pip install -r requirements.txt
```

### 1. Install Ollama
Download from: https://ollama.com/download  
Then run:
```bash
ollama run mistral
```

### 2. Launch the app
```bash
streamlit run app.py
```

---

## 💬 Example questions:
- Who is the head of state?
- What are the rights of citizens?
- What does the Constitution say about education?

---

## 📁 Project Structure

```
ai-constitution-assistant/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .env (optional for OpenAI)
├── chroma_db/
└── screenshots/
```

---

## 🛡 License
MIT License. See `LICENSE` file.

---

## 🧑‍🏫 Authors
This project was developed as part of Blockchain Technologies 2 course at [Your University].

> Group members: Name 1, Name 2, Name 3

---

## 🔗 Submission Instructions
- ✅ Push this project to GitHub
- ✅ Submit GitHub link in Moodle
- ✅ Make sure README.md, LICENSE, and screenshots are included
