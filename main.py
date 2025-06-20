from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MessageInput(BaseModel):
    input: str

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.post("/message")
def post_message(message: MessageInput):
    return {"message": message.input}