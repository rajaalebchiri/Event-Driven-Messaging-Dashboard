from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageInput(BaseModel):
    input: str

messages = [
        {"id": 1, "input": "Hello from user 1"},
        {"id": 2, "input": "Welcome to the messaging system"},
        {"id": 3, "input": "This is a test message"},
        {"id": 4, "input": "Another mock message"},
        {"id": 5, "input": "Final test message"}
    ]

@app.get("/messages")
def hello_world():
    return {"data": messages}

@app.post("/message")
def post_message(message: MessageInput):
    messages.append({"id": len(messages) + 1, "input": message.input})
    return {"message": message.input}