from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_comands import *



app = ApplicationBuilder().token("5787278584:AAGV4j8__BS8NLWGr3GG3vVqwEN9HEFiApM").build()

print('server start')

app.add_handler(CommandHandler("list", list_comand))
app.add_handler(CommandHandler("book", book_comand))
app.add_handler(CommandHandler("new", new_contact_comand))
# app.add_handler(CommandHandler("sum", sum_comand))

app.run_polling()