import datetime
from fastapi import FastAPI
from pydantic import BaseModel

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemtype: str
    description: str
    client: str
    status: str  


repo = []

app = FastAPI()
 


@app.get("/")
def read_root():
    return "hello"