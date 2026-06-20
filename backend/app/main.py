from fastapi import FastAPI

app = FastAPI(title="Pawlytics API")


@app.get("/")
def read_root():
    return {"status": "ok", "service": "pawlytics"}
    
