from fastapi import FastAPI
from pydantic import BaseModel

# Model


class Data(BaseModel):
    x: float
    y: float


app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello World'}


@app.post('/')
def calc(data: Data):
    z = data.x * data.y
    return {'result': z}
