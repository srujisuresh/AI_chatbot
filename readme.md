# 🧠 Historical Figures Chatbot

Chat with legendary historical figures like **Cleopatra**, **Nikola Tesla**, and **Albert Einstein** in real time, powered by **Groq’s LLaMA 3 API**. This project features a beautifully styled HTML frontend and a secure FastAPI backend that handles character-specific AI responses.

---

## 📌 Features

- 🎨 Elegant parchment-themed frontend
- 🤖 AI-generated replies via Groq LLaMA 3 (70B model)
- 🔒 Secure API key handling with `.env`
- 🧭 Choose from multiple historical characters
- 💬 Dynamic, scrollable chat interface

---

## ⚙️ Tech Stack

| Layer      | Technology       |
|------------|------------------|
| Frontend   | HTML, CSS, Vanilla JS |
| Backend    | FastAPI (Python) |
| API        | Groq (LLaMA 3)   |
| Styling    | Google Fonts, CSS Shadows, Gradients |
| Environment | dotenv (`.env`) |

---

## 🚀 Setup Instructions

### 📁 Folder Structure

historical-chatbot/
├── backend/
│ ├── main.py
│ └── .env
├── frontend/
│ └── index.html

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies


pip install fastapi uvicorn python-dotenv requests


Create .env file
In backend/, add your Groq API key:


GROQ_API_KEY="your_actual_groq_api_key_here"


to run,

uvicorn main:app --reload



example input :-

to Cleopatra,
""How did you maintain power in a male-dominated world?""