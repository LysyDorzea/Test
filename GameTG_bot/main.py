# Import the libraries
import random

import telebot
from telebot import types

# # @Tuto_LD_bot

# Create a list
my_list = ['Rock', 'Scissors', 'Paper']
Winner = 'You won!\n Congratulations 👏🏾 '
Loser = 'You lost!\n Better luck next time 😉 '
Raffle = 'It\'s a tie!\n Try again 😎 '

# Create the Telegram bot
bot = telebot.TeleBot(' ')


# Create the bot/start function
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        'Hello! \n I am a bot that can entertain you by playing the classic game "Rock, Scissors, Paper". To start the game, make your choice.'
    )

    # Create the keyboard
    keyboard = types.ReplyKeyboardMarkup(True)
    button_1 = types.KeyboardButton('Rock')
    button_2 = types.KeyboardButton('Scissors')
    button_3 = types.KeyboardButton('Paper')

    keyboard.add(button_1, button_2, button_3)

    bot.send_message(message.chat.id, 'Make your choice.', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message comes from the custom keyboard
    if message.text not in ['Rock', 'Scissors', 'Paper']:
        bot.reply_to(
            message,
            "You selected invalid data. Please use the keyboard created by the bot."
        )
        return

    random_result = random.choice(my_list)
    bot.send_message(message.chat.id, random_result)
    if message.text == 'Rock' and random_result == 'Rock':
        bot.reply_to(message, Raffle)
    elif message.text == 'Rock' and random_result == 'Scissors':
        bot.reply_to(message, Winner)
    elif message.text == 'Scissors' and random_result == 'Scissors' or message.text == 'Paper' and random_result == 'Paper':
        bot.reply_to(message, Raffle)
    elif message.text == 'Scissors' and random_result == 'Paper' or message.text == 'Paper' and random_result == 'Rock':
        bot.reply_to(message, Winner)
    else:
        bot.reply_to(message, Loser)


bot.polling(none_stop=True)
