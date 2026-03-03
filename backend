from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional AI call assistant. Speak politely and concisely."},
            {"role": "user", "content": message.text}
        ]
    )

    return {"reply": response.choices[0].message.content}
