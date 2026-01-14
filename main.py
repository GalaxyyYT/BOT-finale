import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot online come {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    parole_vietate = ["coglione", "succhiami", "vaffanculo"]
    if any(p in message.content.lower() for p in parole_vietate):
        await message.delete()
        await message.channel.send(f"⚠️ {message.author.mention}, moderazione attiva!")
    await bot.process_commands(message)

# Usa il token dalle impostazioni di Render
token = os.getenv('DISCORD_TOKEN')
bot.run(token)
