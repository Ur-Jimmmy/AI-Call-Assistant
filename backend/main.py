from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("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"))

class Message(BaseModel):
    text: str

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
