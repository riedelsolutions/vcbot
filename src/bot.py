import discord
from discord.utils import get
from discord.ext.commands import Bot
from config import BOT_TOKEN, ROLE_NAME, OWNER_ID
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  
   
@client.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    if not get(guild.roles, name=ROLE_NAME):
        await guild.create_role(name=ROLE_NAME)
    if after.channel is None:
        role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
        await member.remove_roles(role)
    elif not before.channel and after.channel:
        role = discord.utils.get(member.guild.roles, name=ROLE_NAME)
        await member.add_roles(role)

client.run("TOKEN")