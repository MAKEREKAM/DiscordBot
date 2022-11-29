import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    await client.change_presence(activity=discord.Game(name=''))
    print("logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user: 
        return

client.run(os.environ['token'])