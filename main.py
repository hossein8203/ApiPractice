from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import json

# Import Classes

app = FastAPI()

# Products

product = []


# Base Models
class User(BaseModel):
    username: str
    password: str


class Admin(BaseModel):
    username: str = "admin"
    password: str = "123456"


class Product(BaseModel):
    code: int
    name: str
    quantity: int
    price: int
    discount: str
    description: str


# Operations


@app.get("/api/hello/")
async def hello(name: str, family: str):
    return {"message": f"hello {name} {family}"}


@app.post("/api/login")
async def login(user: User, response: Response):
    admin = Admin()
    if admin.username == user.username and admin.password == user.password:
        return {"message": "ok"}
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"message": "Authorization failed!"}


@app.post("/api/products/new")
async def create_product(p: Product, response: Response):
    product.append(p)
    response.status_code = status.HTTP_201_CREATED
    return {"message": f"{p.name} {p.code} Successfully Created!"}


@app.get("/api/products/")
async def show_product(response: Response):
    return {"products": product}
