from flask import Flask
import telegram
# Create the application instance
TOKEN ='6244092180:AAH_10MCMX4wAESk6TTp-iboI1EMSe6FeZ8'
bot = telegram.Bot(TOKEN)
chat_id = '1432402481'
app = Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    bot.send_message(chat_id,text="hello word")
    return 'index page'

if __name__=="__main__":
    app.run(debug=True)