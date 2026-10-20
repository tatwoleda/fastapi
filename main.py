#1
from fastapi import FastAPI
from starlette.responses import JSONResponse, PlainTextResponse, HTMLResponse, FileResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"Привет": "Я жму 200"}

#2
app = FastAPI(title="Моё приложение", version="1.0.0")

@app.get("/items")
def get_items():
    return {"items": ["яблоко", "банан"]}

@app.post("/items")
def create_item():
    return {"status": "создано"}

@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"updated": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}

#3
@app.get("/json")
def get_json():
    return {"name": "Иван", "age": 30}

@app.get("/json-status")
def get_json_status():
    return JSONResponse(
        content={"ok": True},
        status_code=201,
        headers={"X-Custom": "value"}
    )

@app.get("/text", response_class=PlainTextResponse)
def get_text():
    return "Это простой текст"

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1>Заголовок</h1><p>Параграф</p>"

#4
@app.get("/download")
def download_file():
    file_path = "static/example.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Содержимое файла для скачивания")
    return FileResponse(
        path=file_path,
        filename="example.txt",
        media_type="text/plain"
    )

#5
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "type": type(user_id).__name__}

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": ""}
    return {"model_name": model_name, "message": ""}