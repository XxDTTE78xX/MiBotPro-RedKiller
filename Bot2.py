import discord
from discord.ext import commands
from psw import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Sistemas listos. Conectado como: {bot.user}')

@bot.command()
async def hello(ctx):
    with open('registro_actividad.txt', 'a') as f:
        f.write(f"El usuario {ctx.author} uso /hello\n")
        
    await ctx.send(f'¡Hola Crack! Me llamaron {bot.user}, pero me puedes decir RedKiller10.')

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="Panel de Control de RedKiller10",
        description="Aquí tienes mis funciones actuales:",
        color=discord.Color.green()
    )
    embed.add_field(name="/hello", value="Saludo del bot.", inline=False)
    embed.add_field(name="/password [número]", value="Genera una clave segura.", inline=False)
    embed.add_field(name="/SaeItoshi", value="Info sobre el mediocampista de Blue Lock.", inline=False)
    embed.add_field(name="/heh [número]", value="Ríete un poco.", inline=False)
    embed.set_footer(text="Proyecto de Programación - Kodland")
    
    await ctx.send(embed=embed)

@bot.command()
async def password(ctx, l=12):
    await ctx.send(f'Tu contraseña segura es: `{gen_pass(l)}`')

@bot.command()
async def SaeItoshi(ctx):
    info = (
        "**Sae Itoshi:** El prodigio de Blue Lock.\n"
        "• **Visión:** Metavisión quirúrgica.\n"
        "• **Rol:** El mejor mediocampista joven del mundo.\n"
        "• **Estilo:** Elegante y eficiente."
    )
    await ctx.send(info)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

bot.run("Aqui_Tu_Token")
