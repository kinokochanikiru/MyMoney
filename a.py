
from fastapi import FastAPI
from pydantic import BaseModel

class Data(BaseModel):
    x: int
    y: int

app = FastAPI()
@app.get("/")
def index():
    return {"message": "Data received successfully"}

@app.post("/")
def calculate(data: Data):
    result = data.x + data.y
    return {"result": result}