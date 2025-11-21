import discord
TOKEN = "put your bot token here"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == client.user:
        return

    # Check if message contains ':3'
    if ":3" in message.content:
        await message.channel.send(
            "TWINK DETECTED",
            file=discord.File("balls.png")  # <-- Replace with your image file
        )


client.run(TOKEN)
