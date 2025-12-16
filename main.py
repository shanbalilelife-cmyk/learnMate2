import asyncio
import os
from threading import Thread
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# تست ساده ربات
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "سلام! ربات روی Render زنده‌ست و کار می‌کنه ✅\n"
        "حالا می‌تونیم گزارش‌گیری دینی و زمان‌بندی رو اضافه کنیم!"
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer("ربات فعاله! پیامت دریافت شد: " + message.text)

# وب‌سرور ساده برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "ربات تلگرام درس‌خوانی زنده‌ست! 🚀"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

async def main():
    print("ربات تلگرام شروع شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    # وب‌سرور در thread جدا
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # ربات تلگرام
    asyncio.run(main())