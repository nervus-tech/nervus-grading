from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Grading Service"}

@app.get("/test")
def read_test():
    return {"message": "Grading Service is running"}