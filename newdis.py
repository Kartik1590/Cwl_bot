import discord
import pytz
from discord.ext import commands
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import datetime
import requests as rq

header = {'Accept':'application/json','authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFlNDgyNDUzLTc2MGEtNDFhMS1iMTc3LWI4ZDkyNzUzYjdkNiIsImlhdCI6MTYzNjM0NjAzNywic3ViIjoiZGV2ZWxvcGVyLzViYjUyNTI2LTNmOGItMzcwZS0wYzlkLTgxZDMwZjI1NjNjOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE1Ny4zMy4yNTIuMTMzIl0sInR5cGUiOiJjbGllbnQifV19.IRRYnCGB11A6fNDQxGAOHBl6FxgiHBKHuipCUf3UWb3ICsGdYvR_GhVAZn8a6FJos6XNPInPjqvIpgdLg46RNw'}


scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/spreadsheets"]
cred=ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
clients=gspread.authorize(cred)
sheet=clients.open("cwl_november_2021").sheet1
token ='NzEzMjgzMjE3Nzg4MjM5ODgy.Xsd2ww.oiHgihLQwLCdAdCbYEyQHYBcSOQ'

month=datetime.datetime.now().strftime('%B')

client=commands.Bot(command_prefix='!',description='honey')
client.remove_command('help')
Th14=[]
Th13=[]
Th12=[]
eligible_draw_player=[]
eligible_draw_th=[]


drawn=[]
town=[]



#starting

@client.event
async def on_ready():
    print('bot is ready')
@client.command()
async def help(ctx):
    author=ctx.message.author
    embed=discord.Embed(
        colour=discord.Colour.red(),
        description='*Here are some usefull commands*'

    )
    embed.set_author(name='Help Command',icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkFAqFNgYwO0GdmcjkkdWpTBZ4nVhl_RptAw&usqp=CAU')
    embed.add_field(name='**1. Player selection for bonus**',value='`!cwl th (enter the value of th eg. th14,th13 and so on)`',inline=False)
    embed.add_field(name='**2. Players eligible for draw bonus**',value='`!lst th`',inline=False)
    embed.add_field(name='**3. Add players in the list**',value='`!add Townhall Player_name (eg !add 14 Honey)`',inline=False)
    embed.add_field(name='**4. Remove players from the list**', value='`!remove Townhall Player_name (eg !remove 14 Honey)`',inline=False)
    embed.add_field(name='**5. Remove players from the Performance list**',value='`!remove_perform Townhall Player_name (eg !remove 14 Honey)`',inline=False)
    embed.add_field(name='**6. Add players in the Performance list**',
                    value='`!add_perform Townhall Player_name (eg !remove 14 Honey)`',inline=False)
    embed.add_field(name='**7. Winners of Performance bonus**', value='`!performance`',inline=False)
    embed.add_field(name='**8. Winners of Draw bonus**', value='`!draw`',inline=False)
    embed.add_field(name='**9. Winners of CWL**', value='`!winner month (eg: !winner october)`',inline=False)
    embed.add_field(name='**10. Select number of performance bonus players **', value='`!select Number_of_player (eg: !select 5)`', inline=False)
    embed.add_field(name='**11. Link of spreadsheet**', value='`!link`', inline=False)
    embed.add_field(name='**12. Can clear performance and drawn list**', value='`!clearList list_name (eg: !clearList performance)`', inline=False)



    embed.set_footer(icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg',text='edited by honey')
    embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkFAqFNgYwO0GdmcjkkdWpTBZ4nVhl_RptAw&usqp=CAU')
    await author.send(author,embed=embed)
    await ctx.send(embed=embed)
@client.command()

async def cwl(ctx,th='th14'):

    if th=='th14':

        select=random.choice(Th14)
        drawn.append(select)
        town.append(th)
        Th14.remove(select)

        new=discord.Embed(colour=discord.Colour.blue(),description=f"Winner of CWL {month.upper()} 2021 from TH14 roaster",timestamp=datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        new.set_author(name='Townhall 14',icon_url='https://i.ytimg.com/vi/hpI9avCutdQ/maxresdefault.jpg')
        new.set_thumbnail(url='https://i.ytimg.com/vi/hpI9avCutdQ/maxresdefault.jpg')
        new.add_field(name=select,value='TH14',inline=False)


        await ctx.send(embed=new)
    elif th=='th13':
        select1 = random.choice(Th13)
        drawn.append(select1)
        town.append(th)
        Th13.remove(select1)

        new1 = discord.Embed(colour=discord.Colour.dark_red(), description=f"Winner of CWL {month.upper()} 2021 from TH13 roaster",
                             )
        new1.set_author(name='Townhall 13', icon_url='https://i.ytimg.com/vi/iWKrwoO6KGQ/maxresdefault.jpg')
        new1.set_thumbnail(url='https://i.ytimg.com/vi/iWKrwoO6KGQ/maxresdefault.jpg')
        new1.add_field(name=select1, value='TH13', inline=False)

        await ctx.send(embed=new1)
    elif th=='th12':
        select2 = random.choice(Th12)

        drawn.append(select2)
        town.append(th)
        Th12.remove(select2)
        new2 = discord.Embed(colour=discord.Colour.dark_green(), description=f"Winner of CWL {month.upper()} 2021 from TH12 roaster")
        new2.set_author(name='Townhall 12', icon_url='https://i.pinimg.com/originals/db/31/15/db31152688e7b48cb16517a8e4d6507e.jpg')
        new2.set_thumbnail(url='https://i.pinimg.com/originals/db/31/15/db31152688e7b48cb16517a8e4d6507e.jpg')
        new2.add_field(name=select2, value='TH12', inline=False)

        await ctx.send(embed=new2)




@client.command()
async def lst(ctx,th='th14'):
    if th=='th14':
        town14 = discord.Embed(colour=discord.Colour.blurple(), description="List of Townhall 14",timestamp=datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        town14.set_author(name='Townhall 14', icon_url='https://i.ytimg.com/vi/hpI9avCutdQ/maxresdefault.jpg')
        town14.set_thumbnail(url='https://i.ytimg.com/vi/hpI9avCutdQ/maxresdefault.jpg')
        for i in range(len(Th14)):
            town14.add_field(name=Th14[i], value='TH14', inline=False)

        await ctx.send(embed=town14)
    elif th=='th13':
        town13 = discord.Embed(colour=discord.Colour.light_grey(), description="List of Townhall 13",timestamp=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                             )
        town13.set_author(name='Townhall 13', icon_url='https://i.ytimg.com/vi/iWKrwoO6KGQ/maxresdefault.jpg')
        town13.set_thumbnail(url='https://i.ytimg.com/vi/iWKrwoO6KGQ/maxresdefault.jpg')
        for i in range(len(Th13)):
            town13.add_field(name=Th13[i], value='TH13', inline=False)

        await ctx.send(embed=town13)
    elif th=='th12':
        town12 = discord.Embed(colour=discord.Colour.dark_green(),
                             description="List of Townhall 12",timestamp=datetime.datetime.now(pytz.timezone('Asia/Kolkata')))
        town12.set_author(name='Townhall 12',
                        icon_url='https://i.pinimg.com/originals/db/31/15/db31152688e7b48cb16517a8e4d6507e.jpg')
        town12.set_thumbnail(url='https://i.pinimg.com/originals/db/31/15/db31152688e7b48cb16517a8e4d6507e.jpg')
        for i in range(len(Th12)):
            town12.add_field(name=Th12[i], value='TH12', inline=False)
        await ctx.send(embed=town12)
    else:
        await ctx.send (f'sorry the townhall i.e *{th}*, you have entered is not in the roster')
@client.command()
async def add(ctx,th=0,*,name):
    if th==14:
        Th14.append(name)
        await ctx.send(f'{name} has been added to the list')
    elif th==13:
        Th13.append(name)
        await ctx.send(f'{name} has been added to the list')
    elif th==12:
        Th12.append(name)
        await ctx.send(f'{name} has been added to the list')
    else:
        await ctx.send("check your input")
@client.command()
async def remove(ctx,Townhall=0,*,name):
    if Townhall==14:
        Th14.remove(name)
        await ctx.send(f'{name} has been removed from list')
    elif Townhall==13:
        Th13.remove(name)
        await ctx.send(f'{name} has been removed from list')
    elif Townhall==12:
        Th12.remove(name)

        await ctx.send(f'{name} has been removed from list')
    else:
        await ctx.send("Please check your inputs")
@client.command()
async def winner(ctx):
    channel=client.get_channel(897735482987925505)
    win=discord.Embed(
        colour=discord.Colour.gold(),
        description='*Winners of Bonus*',
        timestamp=datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

    )
    month=datetime.datetime.now().strftime('%B')
    try:
        win.set_author(name=f'*CWL {month.upper()} 2021*',icon_url='https://static.wikia.nocookie.net/clashofclans/images/c/c0/War_League_Main_Banner.png/revision/latest/scale-to-width-down/300?cb=20181023145516')
    except:
        f"'{month}' please check this value"
    for i in range(len(perform)):
        win.add_field(name=perform[i],value=f'th{townhall[i]}',inline=False)
    for i in range(len(drawn)):
        win.add_field(name=drawn[i], value=town[i], inline=False)
    win.set_footer(text='Edited by honey',icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')

    await ctx.send(embed=win)
    await channel.send(embed=win)


@client.command()
async  def draw(ctx):

    channel = client.get_channel(897735482987925505)
    win1 = discord.Embed(
        colour=discord.Colour.dark_red(),
        description='Draw winners'
    )
    for i in range(len(drawn)):
        win1.add_field(name=drawn[i], value=town[i], inline=False)

    win1.set_footer(text='Edited by honey',
                   icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')
    await ctx.send(embed=win1)
    await channel.send(embed=win1)
    await channel.send(f'Draw result of month {common.month}')
perform=[]
townhall=[]
@client.command()
async def add_perform(ctx,th,*,name):
    perform.append(name)
    townhall.append(th)
    await ctx.send(f'{name} has been added to performer list')
@client.command()
async def remove_perform(ctx,th,*,name):
    perform.remove(name)
    townhall.remove(th)
    await ctx.send(f'{name} has been removed from performer list')
@client.command()
async  def performance(ctx):
    channel = client.get_channel(897735482987925505)

    win2= discord.Embed(
        colour=discord.Colour.blue(),
        description='Performance Winners'
    )
    for i in range(len(perform)):
        win2.add_field(name=perform[i], value=f'th{townhall[i]}', inline=False)
    win2.set_footer(text='Edited by honey',
                    icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')
    await ctx.send(embed=win2)
    await channel.send(embed=win2)
@client.command()
async def Thanks(ctx):
    await ctx.send(f"Thank you so much Honey for creating me")


@client.command()
async def clear(ctx,ammount=1):
    await ctx.channel.purge(limit=ammount)
    await ctx.send(f'**{ammount}  messages has been deleted**')
@client.command()
async def plot(ctx):
    df=pd.read_csv("CWL_A.csv")
    x=df['Total_des']
    y=df["Total_Stars"]
    plt.plot(x, y)
    plt.xlabel("Destruction")
    plt.ylabel("Stars")


    plots= discord.Embed(
    colour=discord.Colour.dark_red(),
        description="Graph",

    )

    plots.set_image(url='')
    
    await ctx.send(embed=plots)


#LIST OF PKJ

'''@client.command()
async def PKJ(ctx):
    new2 = ['Deb', 'Subhajit', 'Roy', 'Prince', 'Rao hamza', 'Worrior king', 'Shoaib', 'Nomad', 'Talha', 'Waqar',
            'Worrior king', 'Hassan', 'Prince', 'Bibrash', 'haris']
    th1 = [14, 14, 14, 13, 13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11]
    pak=discord.Embed(
        colour=discord.Colour.dark_green(),
        description= 'List of PKJ'
    )

    pak.set_thumbnail(url='https://api-assets.clashofclans.com/badges/70/nrF2CIMTEVQOJiHb6DhOkO7Mo2mhM4DloPaWvPaK_7I.png')
    for i in range(0,len(new2)):
        pak.add_field(name=new2[i],value= th1[i])

    pak.set_footer(text='Edited By Honey',icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')
    await ctx.send(embed=pak)
#LIST OF INDIA
@client.command()
async def India(ctx):
    new = ['Honey', 'Raish','RV', 'Nadeem', 'Romen', 'Abhay', 'Rohit', 'ROHIT', 'Bh', 'Arun', 'Neo Blaze', 'Meady', 'Th',
           'Honey1', 'Amish']
    th = [14, 14,14, 13, 13, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11]
    ind=discord.Embed(
        colour=discord.Colour.orange(),
        description='List of India',
        size=1
    )
    ind.set_thumbnail(url='https://api-assets.clashofclans.com/badges/70/lh5138F8tqr755o4PEhvhwnDuJTw4x_eEYCbV9ZU56E.png')
    for i in range(len(new)):
        ind.add_field(name=new[i],value=th[i])

    ind.set_footer(text='Edited By Honey',icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')
    await ctx.send(embed=ind)'''

@client.command()
async def select(ctx,number=0):
    perform.clear()
    drawn.clear()
    eligible_draw_th.clear()
    eligible_draw_player.clear()
    Th14.clear()
    Th13.clear()
    Th12.clear()
    myindex = sheet.col_values(1)[1:number+1]
    for i in myindex:
        perform.append(i)
    mydata = sheet.col_values(2)[1:number+1]
    for i in mydata:
        townhall.append(i)
    myindex1 = sheet.col_values(1)[number+2:]
    for i in myindex1:
       eligible_draw_player.append(i)
    mydata1 = sheet.col_values(2)[number+2:]
    for i in mydata1:
        eligible_draw_th.append(i)

    q=Bonus(len(eligible_draw_th))
    q.select_bonus()
    await ctx.send('`Players selected successfully`')
    await ctx.send(f'Selected Players for Performance Bonus are `{number}`\nSelected Players for Draw Bonus are `{q.length}`.')
@client.command()
async def link(ctx,month):
    if month.lower() == 'october':
        await ctx.send('https://docs.google.com/spreadsheets/d/1XJpsjZz7zWnIBEIHgUF75c65mODWsNkIEAS2EXEqR-A/edit?usp=sharing')
    elif month.lower() =='november':
        await ctx.send('https://docs.google.com/spreadsheets/d/1qoM9CLtD-Gfo441EYiUEng0C75r0F5Zlgd7EJ-eurV4/edit?usp=sharing')

@client.command()
async def clearList(ctx,about):
    author = ctx.message.author
    if about=='performance':
        perform.clear()
        townhall.clear()
    elif about=='draw':
        drawn.clear()
        town.clear()
    else:
        f'`Please check your input "{about}"`'
    await  ctx.send('**List was cleared by **')
    await ctx.send(ctx.author.mention)

class Bonus():
    def __init__(self,length):
        self.length=length
    def select_bonus(self):
        o=list(map(str,eligible_draw_th))
        l=list(zip(o,eligible_draw_player))
        for u,v in l:
            if u=='14':
                Th14.append(v)
            elif u=='13':
                Th13.append(v)
            elif u=='12':
                Th12.append(v)
            else:
                pass

        return 0
@client.command()
async def clan(ctx):
    playerss=[]
    role=[]
    j=rq.get('https://api.clashofclans.com/v1/clans/%23UUYP9JC0/members',headers=header)
    t=j.json()
    for i in range(51):
        try:
            y=t['items'][i]['name']
            playerss.append(y)
            u=t['items'][i]['role']
            role.append(u)
        except:
            pass
    win2 = discord.Embed(
        colour=discord.Colour.blurple(),
        description='Roles'
    )
    for i in range(25):
        win2.add_field(name=playerss[i], value=f'{role[i]}', inline=True)
    win2.set_footer(text='Edited by honey',
                    icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')
    await ctx.send(embed=win2)
    win4 = discord.Embed(
        colour=discord.Colour.blurple(),
        description='Roles'
    )
    for i in range(25,len(role)):
        win4.add_field(name=playerss[i], value=f'{role[i]}', inline=True)
    win4.set_footer(text='Edited by honey',
                    icon_url='https://i.pinimg.com/originals/5b/61/75/5b6175b3e9d50cd026e8111e248cdd26.jpg')
    await ctx.send(embed=win4)

client.run(token)
