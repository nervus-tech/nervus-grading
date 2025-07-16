from fastapi import FastAPI
import os
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Grading Service"}

@app.get("/test")
def read_test():
    return {"message": "Grading Service is running"}