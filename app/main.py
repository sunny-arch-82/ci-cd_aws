from fastapi import FastAPI
import time
import random

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/order")
def process_order(order: dict):
    order_id = order.get("order_id", "unknown")
    processing_time = round(random.uniform(0.5, 2.0), 2)
    time.sleep(processing_time)
    return {
        "status": "processed",
        "order_id": order_id,
        "processing_time": processing_time
    }
