# from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
# from telegram.ext import Application, CommandHandler, ContextTypes

# BOT_TOKEN = "8154701113:AAFyOpD51NConbfTiFJ9TkxLGG00WYz_Sxc"

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [
#             KeyboardButton(
#                 text="Open My App",
#                 web_app=WebAppInfo(url="https://pythondev161221.github.io/Calculator_14042025/")
#             )
#         ]
#     ]
#     reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
#     await update.message.reply_text("Welcome! Click below to open the app:", reply_markup=reply_markup)

# app = Application.builder().token(BOT_TOKEN).build()
# app.add_handler(CommandHandler("start", start))

# app.run_polling()

import os
from flask import Flask, request
from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8154701113:AAFyOpD51NConbfTiFJ9TkxLGG00WYz_Sxc")
WEBHOOK_URL = os.getenv("https://calculator-backend-20z7.onrender.com")  # e.g. https://your-service-name.onrender.com

app = Flask(__name__)
telegram_app = Application.builder().token(8154701113:AAFyOpD51NConbfTiFJ9TkxLGG00WYz_Sxc).build()

# --- Telegram bot handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            KeyboardButton(
                text="Open My App",
                web_app=WebAppInfo(url="https://pythondev161221.github.io/Calculator_14042025/")
            )
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Click below to open the app:", reply_markup=reply_markup)

telegram_app.add_handler(CommandHandler("start", start))

# --- Flask route to receive Telegram updates ---
@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "OK"

# --- Setup webhook on start ---
@app.before_first_request
def init_webhook():
    telegram_app.bot.delete_webhook()
    telegram_app.bot.set_webhook(url=WEBHOOK_URL)

# --- Run the Flask app ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
