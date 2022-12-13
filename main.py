from telegram import Bot
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

bot = Bot(token='5974827277:AAGRWuyiFdcZVPv-_Zqo5FJRE2Gdt7dR8w8')
updater = Updater(token='5974827277:AAGRWuyiFdcZVPv-_Zqo5FJRE2Gdt7dR8w8')
dispatcher = updater.dispatcher

def start(update, context):
    text = update.message.text.split()
    list = []
    for elem in text:
        if 'абв' not in elem:
            list.append(elem)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))


start_hundler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_hundler)

updater.start_polling()
updater.idle()
    