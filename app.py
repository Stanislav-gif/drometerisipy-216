import datetime
from typing import Annotated, Optional
from fastapi import FastAPI, Form
from pydantic import BaseModel

class Order(BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemtype: str
    description: str
    client: str
    status: str 
    master: Optional[str] = "Не назначен"

class UpdateOrderDTO(BaseModel):
    number: int 
    status: Optional[str] = ""
    description: Optional[str] = ""
    master: Optional[str] = ""

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

@app.post("/orders")
def create_order(dto: Annotated[Order , Form()]):
    repo.append(dto)