from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
import requests
import nj_server

ITEM_NAMES = list(nj_server.catalog.keys())

API_URL = "http://localhost:8000/warehouse"

app = FastAPI( title="API Buddy")

app.mount("/static",
          StaticFiles(directory="static"),
          name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request,
        "items": ITEM_NAMES
        }
    )

@app.post("/", response_class=HTMLResponse)
def send(
    request: Request,
    product: str = Form(...),
    oder_qty: int = Form(...)
    ):
    r = requests.get(
        f"{API_URL}/{product}",
        params={"order_qty": oder_qty}
    )
    data = r.json()

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "data": data
        }
    )

