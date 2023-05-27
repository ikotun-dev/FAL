from fastapi import FastAPI
app = FastAPI()
from enum import Enum

class Modelname(Enum):
    alexnet = "alexnet"
    lenet = "lenet"

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

