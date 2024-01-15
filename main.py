import discord
from discord.ext import commands

intents = discord.Intents.all()  # Ative todos os intents


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot está online!')

@bot.command()
async def perfil(ctx, member: discord.Member = None):
    member = member or ctx.author

    # Coleta informações sobre o membro
    joined_at = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")
    created_at = member.created_at.strftime("%Y-%m-%d %H:%M:%S")

    # Cria um embed para o perfil
    embed = discord.Embed(title=f'Perfil de {member.name}', color=discord.Color.blue())
    embed.add_field(name='Nome', value=member.display_name, inline=True)
    embed.add_field(name='ID', value=member.id, inline=True)
    embed.add_field(name='Criado em', value=created_at, inline=False)
    embed.add_field(name='Entrou em', value=joined_at, inline=False)

    # Envia a mensagem do perfil com a opção de reação
    message = await ctx.send(content=f"{member.mention}, clique na reação para definir ou atualizar seu sobremim.", embed=embed)
    await message.add_reaction('✅')

    # Função para verificar reações
    def check(reaction, user):
        return user == member and str(reaction.emoji) == '✅'

    try:
        # Espera pela reação do membro mencionado sem limite de tempo
        reaction, user = await bot.wait_for('reaction_add', check=check)

        # Remove a reação após clicar
        await message.remove_reaction('✅', member)

        # Agora você pode coletar a nova sobremim do usuário mencionado
        await ctx.send(f"{user.mention}, digite sua nova sobremim:")

        def check_message(m):
            return m.author == member and m.channel == ctx.channel

        new_bio_message = await bot.wait_for('message', check=check_message)
        new_bio = new_bio_message.content

        # Envia a mensagem de sobremim em embed
        embed_sobremim = discord.Embed(title=f'Sobremim atualizada para {member.name}', color=discord.Color.green())
        embed_sobremim.add_field(name='Nova Sobremim', value=new_bio, inline=False)
        await ctx.send(embed=embed_sobremim)

    except asyncio.TimeoutError:
        await ctx.send(f"Você não clicou na reação a tempo para atualizar sua sobremim.")



bot.run('MTE5MDEzNzY5NTc3NTc1MjIxMw.G8NBWO.nxY1AXI7KGSrYHdBX-X2zWpMTfhnmujs3N0jwA')
