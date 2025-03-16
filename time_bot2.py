import asyncio
import datetime
from telegram import Bot
from telegram.error import TelegramError

TOKEN = "7719635790:AAFSUtT3PSrWdYqDb0P4pn_Px_LOeNfYBj4"
CHANNEL_ID = "@saatgoiran"

bot = Bot(token=TOKEN)

async def send_time():
    try:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        message = f"⏰ ساعت فعلی: {now}"
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        print(f"✅ پیام ارسال شد: {message}")
    except TelegramError as e:
        print(f"❌ خطا در ارسال پیام: {e}")

async def job_scheduler():
    while True:
        await send_time()
        await asyncio.sleep(60)  # هر ۶۰ ثانیه اجرا شود

print("✅ ربات شروع به کار کرد...")
asyncio.run(job_scheduler())
