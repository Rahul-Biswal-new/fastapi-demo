from fastapi import FastAPI
app= FastAPI()

# amazon.com/delete-user 
@app.get("/")
def index():
    return {"name": "first-data"}