import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
from discord import Game


bot = commands.Bot(command_prefix='=')
startup_extensions = ['Music']

@bot.event
async def on_message(message):
    if message.content.startswith("ping"):
        await bot.send_message(message.channel, "Pong")

    await bot.process_commands(message)

class Main_Commands() :
    def __init__(self, bot):
        self.bot = bot

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name='With NOWAYS Heart'))
    print('Ready, Freddy')
    
@bot.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await bot.send_message(member, 'Welcome To Bikini Bottom Please Enjoy Your Stay')
    print('Sent message to ' + member.name)

@bot.event
async def on_message(message):
    if message.content == 'Hi':
        await bot.send_message(message.channel,'Hey there bby')
          
@bot.event
async def on_message(message):
    if message.content == 'Skywalker':
        await bot.send_message(message.channel,'The Creator')
    if message.content == 'Kapo':
        await bot.send_message(message.channel,'LOL Master')
    if message.content == 'Fouad':
        await bot.send_message(message.channel,'The Boss')
    if message.content == 'Mido':
        await bot.send_message(message.channel,'Mido El Moz Uff A77')        
    if message.content == 'Omar':
        em = discord.Embed(description='Ladies Please')
        em.set_image(url='https://www.apherald.com/ImageStore/images/politics/politics_analysis/ladies-please-control-647x450.jpg')
        await bot.send_message(message.channel, embed=em)
    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '(): ()' .format(type(e).__name__, e)
            print('Failed to load extension ()\n()' .format(extension,exc))



bot.run('NTE4OTQ3NDkwODc2MjI3NTg0.Duiumw.K11Tjv7uHfjAuE2jHVlja48KAJE')

