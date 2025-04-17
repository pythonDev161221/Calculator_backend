from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8154701113:AAFyOpD51NConbfTiFJ9TkxLGG00WYz_Sxc"

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

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

