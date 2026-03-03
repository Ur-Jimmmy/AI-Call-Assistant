from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# IMPORTANT: do NOT hardcode the key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Message(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "AI Call Assistant running"}

@app.post("/chat")
async def chat(message: Message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": message.text}
        ]
    )
    return {"reply": response.choices[0].message.content}
