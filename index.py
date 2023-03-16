import os
import requests
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API_KEY = os.getenv('API_KEY')

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if not message.content:
        return

    url = 'https://api.kayle.ai/v1/moderate'
    payload = {
        'message': message.content,
        'key': API_KEY
    }

    response = requests.post(url, data=payload)

client.run(TOKEN)
