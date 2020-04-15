import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

   
@client.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    await guild.create_role(name="vc")
    if not before.channel and after.channel:
        role = discord.utils.get(member.guild.roles, name="vc")
        await member.add_roles(role)
    elif before.channel and not after.channel:
        role = discord.utils.get(member.guild.roles, name="vc")
        await member.remove_roles(role)

client.run("BOT_TOKEN")