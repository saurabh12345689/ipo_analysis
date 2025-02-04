from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# Mount the static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template folder
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Placeholder pages for other links
@app.get("/products", response_class=HTMLResponse)
async def products(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/stock-market", response_class=HTMLResponse)
async def stock_market(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/brokers", response_class=HTMLResponse)
async def brokers(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def login():
    # Login logic here (this is just a placeholder)
    return {"message": "Login Page"}
