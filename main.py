import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  activity = discord.Activity(name = "ten serwer monkaS", type=discord.ActivityType.watching)
  await client.change_presence(activity=activity)
  channel = client.get_channel(822922658294923264)
  embedVar = discord.Embed(title="Online", description="Bot wystartował.", color=0x4287f5)
  await channel.send(embed=embedVar)
  print("Bot się uruchomił.")

@client.command()
async def ping(ctx):
  await ctx.send('Pong!')

@client.command()
async def op(ctx):
  await ctx.send("Zabrano ci uprawnienia administracyjne.")

keep_alive()
client.run(os.getenv('TOKEN'))