from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace * with your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class ChatRequest(BaseModel):
    message: str
    figure: str

character_prompts = {
    "cleopatra": "You are Cleopatra, Queen of Egypt. Respond with grace and wit.",
    "tesla": "You are Nikola Tesla. Respond with futuristic vision and brilliance.",
    "einstein": "You are Albert Einstein. Respond with intellect and humor.",
}

@app.post("/chat/")
def chat(req: ChatRequest):
    system_prompt = character_prompts.get(req.figure, "")
    user_message = req.message

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=body
    )

    if response.status_code == 200:
        content = response.json()
        return {"reply": content["choices"][0]["message"]["content"]}
    else:
        return {"reply": "Sorry, something went wrong."}
