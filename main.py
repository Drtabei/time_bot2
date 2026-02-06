
import requests
import asyncio
from telethon import TelegramClient
import os

api_id = 22469157
api_hash = "acfada75b11b221d6e7023a4de8f6803"
channel = "@testachbar"
weather_api = "c20d15117464c4f8a55c582ea6badddb"

cities = [
"Tehran","Karaj","Isfahan","Shiraz","Tabriz","Mashhad","Ahvaz","Qom",
"Kermanshah","Urmia","Rasht","Sari","Bandar Abbas","Arak","Yazd",
"Kerman","Sanandaj","Ilam","Birjand","Zanjan","Qazvin","Semnan",
"Bojnord","Yasuj","Bushehr","Khorramabad","Shahrekord","Gorgan",
"Zahedan","Hamedan","Ardabil"
]

client = TelegramClient("session", api_id, api_hash)

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric&lang=fa"
        r = requests.get(url, timeout=10).json()
        temp = r["main"]["temp"]
        desc = r["weather"][0]["description"]
        return temp, desc
    except:
        return None, None

async def loop_send():
    await client.start()
    print("BOT RUNNING")

    while True:
        for c in cities:
            temp, desc = get_weather(c)

            if temp is None:
                text = f"❌ {c}\nخطا در دریافت هوا"
            else:
                text = f"🌤 {c}\n🌡 دما: {temp}°C\n📝 وضعیت: {desc}"

            await client.send_message(channel, text)
            await asyncio.sleep(2)

        await asyncio.sleep(3600)

with client:
    client.loop.run_until_complete(loop_send())
