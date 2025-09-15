from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str


@app.post("/message")
def get_message(msg: Message):
    #tee jotain viestin kanssa, käännä, muokkaa...
    processed = msg.text.upper()
    return {"processed text": processed}
## tai pelkkä return {"response": f"Vastaanotettu viesti: {msg.text}"}






