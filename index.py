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
async def on_guild_join(guild):
    # Create a new role with the desired color
    role = await guild.create_role(name="KayleAI Role", color=discord.Color(0x34d399), reason="Set bot color to green")

    # Assign the new role to the bot
    bot_member = guild.get_member(client.user.id)
    await bot_member.add_roles(role)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # if message empty
    if not message.content:
        return
    # Print the content of the message to the console
    #print(f'Message from {message.author}: {message.content}')

    url = 'https://api.kayle.ai/v1/moderate'
    payload = {
        'message': message.content,
        'key': API_KEY
    }

    response = requests.post(url, data=payload)
    
    # Uncomment this line to print the response from the API (TODO: Good for debugging)
    #print(response.text)

client.run(TOKEN)
