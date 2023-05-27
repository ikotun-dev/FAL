from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
app = FastAPI()
from enum import Enum

class Modelname(Enum):
    alexnet = "alexnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str 
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
def root():
    return { 'message'  : 'Hello World' }

@app.get("/code/{modelname}")
def data(modelname :Modelname):
    if modelname is Modelname.alexnet : 
        return {'name ' : 'correct name'}
    if modelname.value == "lenet":
        return {"name" : "correct also"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/code/{value}")
def data(value :int):
    return{ 'data value' : value}

@app.post("/items")
async def create_item(item: Item):
    return item