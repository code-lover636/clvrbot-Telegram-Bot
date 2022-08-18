import telegram.ext
import riddles

apiKey = "5705845471:AAESaX_49hrcG1PA2YgoCED0xYs9Fth5D9A"
question = tuple()

def start(update, context):
    msg = """
    Hey! Are you bored?🥱
I'm a bot to help you think and laugh!😂
Type /help to see what I can do.
    """
    update.message.reply_text(msg)
    
def help(update, context):
    msg = """
    Use the following commands to interact with me:
/start - Start the bot
/about - See information about the bot and creator
/ask - I will ask you a riddle
/answer - Find the answer to the riddle
  
Are you lazy to type? You can also click the above links to send commands.
    """
    update.message.reply_text(msg)

def about(update, context):
    msg = """
    clvrbot can ask you riddles and help you think and laugh.
This bot is made with Python Programming Language.
Creator & Owner: Aravind Ashokan
    """
    update.message.reply_text(msg)

def ask(update, context):
    global question
    question = riddles.random_riddle()
    update.message.reply_text(question[1])
    
def answer(update, context):
    global question
    if len(question) == 0:
        update.message.reply_text("I haven't asked any riddle yet. Type /ask to ask a riddle.")
    update.message.reply_text(question[2])
    
updater = telegram.ext.Updater(apiKey, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("about", about))
disp.add_handler(telegram.ext.CommandHandler("ask", ask))
disp.add_handler(telegram.ext.CommandHandler("answer", answer))

 updater.start_polling()
updater.idle()
