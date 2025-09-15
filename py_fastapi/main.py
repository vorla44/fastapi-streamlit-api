from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tai rajaa vain streamlit.io
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Message(BaseModel):
    text: str

@app.post("/message")
def get_message(msg: Message):
    #tee jotain viestin kanssa, käännä, muokkaa...
    processed = msg.text.upper()
    return {"processed text": processed}
## tai pelkkä return {"response": f"Vastaanotettu viesti: {msg.text}"}






