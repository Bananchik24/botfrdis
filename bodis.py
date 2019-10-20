import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix= '*')

@Bot.event
async def on_ready():
    print("Я онлайн")

@Bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello my friend {author.mention}")
    
@Bot.command()
async def Путин(ctx):
    await ctx.send("вор")

@Bot.command()
async def  id(ctx):
    await ctx.send("Твой id: {}".format(ctx.message.author))
    
token = os.environ.get("BOT_TOKEN")

Bot.run(token)
