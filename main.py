from fastapi import FastAPI

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
