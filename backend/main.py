from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Assistant backend is running!"}