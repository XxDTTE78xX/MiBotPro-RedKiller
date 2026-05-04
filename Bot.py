import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sistema de Respaldo: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send(f"¡Hola {message.author.name}!")
    
    elif message.content.startswith('/bye'):
        await message.channel.send("\U0001f642")

    else:
        with open('historial_mensajes.txt', 'a', encoding='utf-8') as f:
            f.write(f"[{message.author}]: {message.content}\n")

client.run("Aqui_Tu_Token")
