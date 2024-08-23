from telegram.ext import Updater, CommandHandler, MessageHandler
import logging
from lexica import AsyncClient
import app

logging.basicConfig(level=logging.INFO)

TOKEN = '6888951177:AAEZMoJqLyS6hxxJrPpUfF2MJ8mi_WjD27k'

async def chat_completion(prompt, model):
    client = AsyncClient()
    output = await client.ChatCompletion(prompt, model)
    return output['content']

def start(update, context):
    context.bot.send_message(chat_id=(link unavailable), text="Hello! I'm your AI chatbot.")

def message_handler(update, context):
    prompt = update.message.text
    model = 'bard'  # yeh model ko aap apne hisab se change kar sakte hain
    output = chat_completion(prompt, model)
    context.bot.send_message(chat_id=(link unavailable), text=output)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text & (~Filters.command), message_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
