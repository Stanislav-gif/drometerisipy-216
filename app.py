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


repo = [
    Order(
        number = 1,
        startDate = "2024-12-05",
        device = "123",
        problemtype = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    )
]
app = FastAPI()

@app.get("/orders")
def get_orders():
    return repo