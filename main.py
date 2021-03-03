from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler



TOKEN =  "1648125639:AAGmJXWf-Psp_IVOVH_hoOPAAJy7BT3BxQA"
def main():
    updater = Updater(token=TOKEN)    # объект, который ловит сообщения из телеграм
    dispatcher = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)   # отфильтровываем сообщения: теперь устройство должно реагировать
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)


    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()


def do_echo(update: Update, context):
    user = update.message.from_user.is_bot
    name = update.message.from_user.first_name
    if user == True:
        update.message.reply_text(text=f"Ты - бот! Уходи отсюда!!!")
    else:
        update.message.reply_text(text=f"ААААА! {name} что ты делаешь?")
        update.message.reply_text(text= "Я не понимаю")

def do_start(update, context):
    update.message.reply_text(text="Ты запустил меня человек")      # текст сообщения, который бот автоматически будет выдавать

def do_help(update, context):
    update.message.reply_text(text="что случилось? Всё ж было норм")


main()