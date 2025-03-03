from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "it's my first depolyment"}
