import telebot

bot = telebot.TeleBot("1726681314:AAFhj0l-djAxu1bd7HxafgJNBDI5FjkoM-M")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет я пока могу только повторять за тобой! Напиши сообщение:")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()