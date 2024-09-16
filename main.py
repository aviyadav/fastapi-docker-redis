from fastapi import FastAPI
import redis


app = FastAPI()

r = redis.Redis(host="redis", port=6379, db=0)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Docker and Redis"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):

    r.set(f"item_{item_id}", q or "No Query")
    cached_value = r.get(f"item_{item_id}")
    return {"item_id": item_id, "q": cached_value}