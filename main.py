from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ["BOT_TOKEN"]
print("BOT_TOKEN loaded, length:", len(TOKEN))
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("GIGL Bot çalışıyor ✅")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
