import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


load_dotenv()

BOT_USERNAME = "@NyoozBot"

# Commands
async def start_commmand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I can fetch tech news")

async def help_commmand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "I am NyoozBot and I can tell you news about technology \n\n"
        "Commands: \n"
        "/start - to start the bot\n"
        "/custom - this is a custom command\n" 
    )
    await update.message.reply_text(text= help_text, parse_mode='Markdown')

async def custom_commmand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is a custom command")

# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good'
    
    if 'news' in processed:
        return 'I can fetch some news for you!'
    
    return 'I do not understand'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_type: str = update.message.chat.type
    incoming_text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {chat_type}: "{incoming_text}"')

    if chat_type == 'group':
        if BOT_USERNAME in incoming_text:
            new_text: str = incoming_text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(incoming_text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(os.getenv('TOKEN')).build()

    # await app.bot.set_my_commands([
    # ("start", "Start the bot"),
    # ("help", "Show help"),
    # ("custom", "custom command"),
    # ])
    
    # Commands
    app.add_handler(CommandHandler('start', start_commmand))
    app.add_handler(CommandHandler('help', help_commmand))
    app.add_handler(CommandHandler('custom', custom_commmand))

    # Messages 
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Poll
    print('Polling...')
    app.run_polling(poll_interval=3)













# if __name__ == "__main__":
#     main()
