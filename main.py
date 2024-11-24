import disnake
from disnake.ext import commands
from servers import servers_class1, servers_class2
from forume_sections import sections_class1, sections_class2
from servers_ip import api_class1, api_class2
from admins import admins_class
from Nicknames import nickname
from Passwords import password_func
import disnake.ext
import disnake.ext.commands

intents = disnake.Intents.default()
intents.message_content = True

bot =  commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    print(f"bot {bot.user} is ready to work")



@bot.slash_command(description = "Сгенерировать никнейм")
async def generate_nickname(interaction: disnake.ApplicationCommandInteraction):

    nick = nickname()
    emb = disnake.Embed(title = f"{nick}", color = disnake.Colour.dark_gray())

    if interaction.guild == None :
        await interaction.response.send_message(embed=emb)

    else :
        await interaction.response.send_message("Проверьте личные сообщения")
        await interaction.author.send(embed=emb)



@bot.slash_command(description = "Сгенерировать пароль")
async def generate_password(interaction: disnake.ApplicationCommandInteraction):

    password = password_func()
    emb = disnake.Embed(title = f"{password}", color = disnake.Colour.dark_gray())

    if interaction.guild == None :
        await interaction.response.send_message(embed=emb)
    else :
        await interaction.response.send_message("Проверьте личные сообщения")
        await interaction.author.send(embed=emb)



@bot.slash_command(description="Дискорд серверы")
async def discord_servers(interaction: disnake.ApplicationCommandInteraction):

    view1 = servers_class1()
    view2 = servers_class2()

    emb = disnake.Embed(title = "Выберите интересующий сервер :", color = disnake.Colour.dark_gray())

    if interaction.guild == None :
        await interaction.response.send_message(embed=emb)
        await interaction.author.send(view=view1)
        await interaction.author.send(view=view2)

    else :
        await interaction.response.send_message("Проверьте личные сообщения")
        await interaction.author.send(embed=emb)
        await interaction.author.send(view=view1)
        await interaction.author.send(view=view2)




@bot.slash_command(description="Разделы форумов")
async def forume_sections(interaction: disnake.ApplicationCommandInteraction):

    view1 = sections_class1()
    view2 = sections_class2()

    emb = disnake.Embed(title = "Выберите интересующий форум :", color = disnake.Colour.dark_gray())

    if interaction.guild == None :
        await interaction.response.send_message(embed=emb)
        await interaction.author.send(view=view1)
        await interaction.author.send(view=view2)

    else :
        await interaction.response.send_message("Проверьте личные сообщения")
        await interaction.author.send(embed=emb)
        await interaction.author.send(view=view1)
        await interaction.author.send(view=view2)




@bot.slash_command(description="Айпи серверов")
async def servers_ip(interaction: disnake.ApplicationCommandInteraction):

    view1 = api_class1()
    view2 = api_class2()

    emb = disnake.Embed(title = "Выберите интересующий айпи адрес :", color = disnake.Colour.dark_gray())

    if interaction.guild == None :
        await interaction.response.send_message(embed=emb)
        await interaction.author.send(view=view1)
        await interaction.author.send(view=view2)

    else :
        await interaction.response.send_message("Проверьте личные сообщения")
        await interaction.author.send(embed=emb)
        await interaction.author.send(view=view1)
        await interaction.author.send(view=view2)




@bot.slash_command(description="Связаться с руководством")
async def contact_to_managment(interaction: disnake.ApplicationCommandInteraction):

    view1 = admins_class()

    emb = disnake.Embed(title = "Выберите с администрацией какого сервера вам нужно связаться :", color = disnake.Colour.dark_gray())

    if interaction.guild == None :      # in dm
        await interaction.response.send_message(embed=emb)
        await interaction.author.send(view=view1)
    else :      # in global chat
        await interaction.response.send_message("Проверьте личные сообщения")
        await interaction.author.send(embed=emb)
        await interaction.author.send(view=view1)





with open('TOKEN', 'r') as file:
    token = file.read()

bot.run(token)
