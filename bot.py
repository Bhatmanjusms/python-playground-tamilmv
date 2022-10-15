from aiogram import *
from aiogram.types import *
import requests
from bs4 import BeautifulSoup
import re
import telebot
import send

bot = Bot(token="5613970727:AAFvGY33k5mSXZ1IXnDCUG_pJjXTfo0oixM")
dp = Dispatcher(bot)
bot = telebot.TeleBot('5613970727:AAFvGY33k5mSXZ1IXnDCUG_pJjXTfo0oixM')


button1 = telebot.types.InlineKeyboardButton(text="⚡Powered by ",url='https://t.me/heyboy2004')

keyboard = telebot.types.InlineKeyboardMarkup().add(telebot.types.InlineKeyboardButton('👨‍💻 Developed by', url='github.com/shinas101')).add(button1)

@dp.message_handler(commands=['start'])
def random_answer(message):
    mssg = '@'+message.from_user.username+' has started the bot 🤖'
    send.send(-1001850194136,mssg)
    bot.send_message(chat_id=message.chat.id,text=f"Hey 👋 {message.from_user.mention}\n\n* Get latest Movies from 1Tamilmv\n⚙️*How to use me??*🤔\nplease Enter */view* command*😌\n\nShare and Support💝",parse_mode='Markdown',reply_markup=keyboard)
            
@dp.message_handler(commands=['view'])
def random_value(message):
    mssg = '@'+message.from_user.username+' has clicked view 👀'
    send.send(-1001850194136,mssg)
    bot.send_message(message.chat.id,text="*Wait for 10 seconds*",parse_mode='Markdown')
    ml = tamilmv()
    for i in ml:
        bot.send_message(chat_id=message.chat.id,text=i,parse_mode='Markdown')

@dp.message_handler(commands=['help'])
def help_command(message):
   bot.send_message(message.chat.id,reply_markup=keyboard)

def tamilmv():

    mainUrl = 'https://www.1tamilmv.hair/index.php'
    mainlink = []

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-G-US;q=0.9,en;q=0.8',
        'Connection':'Keep-alive',
        }

    web = requests.get(mainUrl,headers=headers)
    soup = BeautifulSoup(web.text,'lxml')
    linker = []
    magre = []

    temps = soup.find_all('span',{'class' : 'ipsType_break ipsContained'})

    for i in range(15):
        title = temps[i].findAll('a')[0].text
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)

    for url in linker:
        html = requests.get(url)
        soup = BeautifulSoup(html.text,'lxml')
        pattern=re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        bigtitle = soup.find_all('a')
        alltitles = []
        filelink = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])

        for a in soup.findAll('a',{"data-fileext":"torrent",'href':True}):
            filelink.append(a['href'])

        for title in bigtitle:
            if title.find('span') == None:
                pass
            else:
                if title.find('span').text.endswith('torrent'):
                    alltitles.append(title.find('span').text[20:-8])

        for p in range(0,len(mag)-1):
            # print(filelink[l])
            try:
                mainlink.append(f"*{alltitles[p]}* -->      🧲 `{mag[p]}`                              🗒️->[Torrent file]({filelink[p]})")
            except:
                return mainlink
            # print(f"{titles[i][:-8]} -->  {mag[i]}")

    return mainlink
        


executor.start_polling(dp)
