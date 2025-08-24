import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# yaha apna BotFather se liya hua token daalein
BOT_TOKEN = "8366987051:AAGhNF4F1-ums6vSvSjY-iC4RYOi3zoTHzQ"

# aapka api url
API_URL = "https://osintapi.store/cutieee/api.php?key=jerry&type=mobile&term="

# start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Mujhe ek mobile number bhejo, mai API se result launga 📲")

# jab user number bheje
async def fetch_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = update.message.text.strip()
    url = API_URL + number
    response = requests.get(url)

    if response.status_code == 200:
        data = response.text
        await update.message.reply_text(f"🔎 API Result:\n{data}")
    else:
        await update.message.reply_text("❌ API se data fetch karne me error aaya.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fetch_data))

    print("🤖 Bot chal raha hai...")
    app.run_polling()

if __name__ == "__main__":
    main()
