import discord
from discord.ext import commands
import asyncio
import random
import datetime
import json
from gtts import gTTS
from playsound import playsound

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-',intents = intents)
bot.remove_command("help")

with open('config.json', 'r', encoding='utf8') as f:
    config = json.load(f)

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def help(ctx):
    with open('help.txt', 'r') as f:
        text = f.read()
    embed=discord.Embed(title="幫助help", description=text, color=0x34363c)
    await ctx.send(embed=embed)

@bot.event
async def on_message(msg):
    user_id = config['user']
    user = bot.get_user(user_id)
    if user.mentioned_in(msg):
        text = f"{msg.author.name}在{msg.guild.name}伺服器{msg.channel.name}頻道提及了你"
        s = gTTS(text=text, lang='zh')
        s.save('mention.mp3')
        playsound('mention.mp3')
  
        











bot.run(config['token'])