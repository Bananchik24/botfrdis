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
    author = ctx.message.author
    await ctx.send("вор")

@Bot.command()
async def го играть(ctx):
    everyone = ctx.message.everyone
    await ctx.send(f"го играть {everyone.mention}")
    
token = os.environ.get("BOT_TOKEN")

Bot.run(token)
