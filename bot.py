import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.environ["BOT_TOKEN"]


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    if "diskwala.com" not in url:
        await update.message.reply_text("DiskWala link bhejo.")
        return

    await update.message.reply_text(
        "⏳ DiskWala link receive ho gaya.\n"
        "Direct video resolver available ho to video send hogi."
    )

    # Yahan DiskWala resolver lagta hai.
    # Direct resolver/API ke baghair DiskWala /app/ link
    # ko direct MP4 samajh kar download nahi kiya ja sakta.


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle
    )
)

print("Bot running...")
app.run_polling()
