from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/add")
def add(a:int,b:int):
    return{"sum":a+b}


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "description": "Dell Laptop"
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 20000,
        "description": "Samsung Mobile"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000,
        "description": "Wireless Headphones"
    }
]


# Product List API
@app.get("/products")
def product_list():
    return {
        "success": True,
        "count": len(products),
        "data": products
    }

users=[]
class User(BaseModel):
    email: str
    password:str
@app.post("/signup")
def signup(user: User):
    users.append(user.dict())
    return {
        "message": "Signup successful",
        "user": user.email
    }
@app.get("/welcome")
def welcome():
    return {
        "message": "Welcome to FastAPI"
    }