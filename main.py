import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from contextlib import asynccontextmanager
from config.net import url_webhook
from create_bot import bot, dp
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, Update
from aiogram import F

@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(url=url_webhook+"/webhook",
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)
# app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

@dp.message()
async def start(message: Message) -> None:
    await message.answer('Привет!')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    print("somethink")
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)
