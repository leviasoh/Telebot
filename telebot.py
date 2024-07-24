import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import pyrebase
from collections.abc import MutableMapping

firebaseConfig = {
    'apiKey': "AIzaSyBcAfoXyh-aRxatcWDOiSHpASN3BakbcXA",
    'authDomain': "autobot-13dc0.firebaseapp.com",
    'databaseURL': "https://autobot-13dc0-default-rtdb.firebaseio.com",
    'projectId': "autobot-13dc0",
    'storageBucket': "autobot-13dc0.appspot.com",
    'messagingSenderId': "508703322520",
    'appId': "1:508703322520:web:298474815d6bcbc04c3bed",
    'measurementId': "G-08CNR6EB98"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

BOT_TOKEN = "7348062357:AAGLf07-uT40PVhxJ7y59whjdWW2xdiDq9M"
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.user_data['email'] = ""
    update.message.reply_text("Welcome! Please provide your username. It should consist of only letters (a-z), numbers (0-9), and the characters ‘.’ and ‘_’ .")

def handle_credentials(update, context):
    email = update.message.text + "@auto.bot"

    try:
        # Create user with email and password
        user = auth.create_user_with_email_and_password(email, "123456")
        uid = user['localId']
        update.message.reply_text(f"Your account has been successfully created! Your username is:\n{email}")
    except Exception as e:
        update.message.reply_text(f"Error creating account: {str(e)}")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text & ~Filters.command, handle_credentials)
dispatcher.add_handler(message_handler)

updater.start_polling()
