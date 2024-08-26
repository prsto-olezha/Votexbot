from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, Update
from aiogram.fsm.context import FSMContext
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import uvicorn
import src.FSM as FSM
from main import app, templates
from create_bot import bot, dp

