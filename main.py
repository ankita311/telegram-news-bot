import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


load_dotenv()

# logger = logging.getLogger(__name__)


# Commands
async def start_commmand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I can fetch tech news")






# if __name__ == "__main__":
#     main()
