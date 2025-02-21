from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}


@app.get("/greet/")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

from pydantic import BaseModel

# Define a model for request body validation
class User(BaseModel):
    name: str
    age: int

@app.post("/users/")
def create_user(user: User):
    return {"message": f"User {user.name} of age {user.age} created!"}
