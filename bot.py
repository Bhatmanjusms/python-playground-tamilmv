from aiogram import *
from aiogram.types import *
import requests
from bs4 import BeautifulSoup
import re
import telebot

bot = Bot(token="5506422969:AAEkz2RyxOHiN7ir0poytlepyRvQYpsdQ0E")
dp = Dispatcher(bot)
bot = telebot.TeleBot('5506422969:AAEkz2RyxOHiN7ir0poytlepyRvQYpsdQ0E')

button = InlineKeyboardButton(text="View ", callback_data="view_web")
button1 = InlineKeyboardButton(text="Refresh", callback_data="randomvalue_of100")
keybord_inline = InlineKeyboardMarkup().add(button, button1)

tracker = '&tr=udp://tracker.openbittorrent.com:80/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://tracker.trackerfix.com:81/announce&tr=udp://9.rarbg.me:2730/announce&tr=udp://9.rarbg.to:2730/announce&tr=udp://tracker.fatkhoala.org:13760/announce&tr=udp://tracker.slowcheetah.org:14800/announce&tr=http://tracker.opentrackr.org:1337/announce&tr=udp://tracker.tiny-vps.com:6969/announce'

@dp.message_handler(commands=['start'])
def random_answer(message):
   bot.send_message(chat_id=message.chat.id,text='*please Enter /view command*',parse_mode='Markdown')

@dp.message_handler(commands=['view'])
def random_value(message):
        bot.send_message(chat_id=message.chat.id,text="*Wait for 10 seconds*",parse_mode='Markdown')
        ml = tamilmv()
        for i in ml:
            bot.send_message(chat_id=message.chat.id,text=i,parse_mode='Markdown')

def tamilmv():

    mainUrl = 'https://www.1tamilmv.hair/index.php'
    mainlink = []

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
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
        titles = []
        filelink = []
        mag = pattern.findall(str(bigtitle))
        for a in soup.findAll('a',{"data-fileext":"torrent",'href':True}):
            filelink.append(a['href'])

        for title in bigtitle:
            if title.find('span', attrs={'style':'color:#0000ff;'}) == None:  
                if title.find('span', attrs={'style':'color:#3333ff;'}) != None:
                    titles.append(title.find('span', attrs={'style':'color:#3333ff;'}).text)
            else:
                if title.find('span', attrs={'style':'color:#0000ff;'}) != None:
                    titles.append(title.find('span', attrs={'style':'color:#0000ff;'}).text)

        for l in range(0,len(mag)-1):
            mainlink.append(f"*{titles[l][20:-8]}* -->      🧲 `{mag[l]}{tracker}`                                🗒️->[Torrent file]({filelink[l]})")
            # print(f"{titles[i][:-8]} -->  {mag[i]}")
            
    return mainlink
        


executor.start_polling(dp)
