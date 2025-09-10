import telebot

# Apna bot token yahan paste karo
BOT_TOKEN = "8231793753:AAEancUDIgpZqlVqHHoUqAlF43pws_M8zuA"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to Premium Earning Bot!\nComplete tasks & earn rewards.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "📌 Commands:\n/start - Start bot\n/help - Help menu")

print("🤖 Bot is running...")
bot.polling()
