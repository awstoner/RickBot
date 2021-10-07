import discord
#import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.endswith('huh Rick?'):
        await message.channel.send('Nahh... we doin thighs.')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

#client.run(os.getenv('TOKEN'))
client.run("ODgxOTI2MjQxMjQwODk5NjA0.YSz70Q.EET5gAoEmG69g6d6KXWmfvR10as")