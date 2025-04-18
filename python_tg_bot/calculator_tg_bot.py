


import os
import asyncio
from flask import Flask, request
from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Load Environment Variables ---
BOT_TOKEN = os.getenv("8154701113:AAH-1rDg_6wq9VUy5-unFpOhphRQ8TN5Oy0")
WEBHOOK_URL = os.getenv("https://calculator-backend-wbrx.onrender.com")

print("DEBUG BOT_TOKEN =", {BOT_TOKEN})
print("DEBUG WEBHOOK_URL =", {WEBHOOK_URL})

# --- Flask App ---
app = Flask(__name__)

# --- Telegram Bot App ---
telegram_app = Application.builder().token(BOT_TOKEN).build()

# --- Telegram Handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(
            text="Open My App",
            web_app=WebAppInfo(url="https://pythondev161221.github.io/Calculator_14042025/")
        )]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Click below to open the app:", reply_markup=reply_markup)

telegram_app.add_handler(CommandHandler("start", start))

# --- Flask Route to Receive Webhook Updates ---
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    asyncio.run(telegram_app.process_update(update))
    return "OK"

# --- Setup Webhook on First Request ---
@app.before_first_request
def init_webhook():
    try:
        telegram_app.bot.delete_webhook()
        success = telegram_app.bot.set_webhook(url=WEBHOOK_URL)
        print("Webhook set:", success)
    except Exception as e:
        print("Error setting webhook:", e)

# --- Run Flask App ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

