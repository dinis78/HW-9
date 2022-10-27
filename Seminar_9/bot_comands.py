from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime





async def book_comand (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/list\n/new contact\n/book')    

async def new_contact_comand (update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text


    items = msg.split()
    surname = items[1]
    name = items[2]
    num = items[3]
    book_phon = ('\n'+'Фамилия: ' + surname +','+ ' Имя: ' + name+',' + ' телефон- ' + num + '\n')
    with open ('phon_file_one.txt', 'a', encoding='utf-8') as file_phone:
        file_phone.write(book_phon)
    print (msg)
    
    await update.message.reply_text(f'Фамилия: {surname}, Имя: {name}, телефон- {num}')

async def list_comand (update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open ('phon_file_one.txt', 'r+', encoding='utf-8') as file_phone:
        file=file_phone.read()
    await update.message.reply_text(f'  {file}')