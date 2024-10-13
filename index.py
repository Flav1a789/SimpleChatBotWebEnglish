from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer #Takes a list and gives the best reposnse to h
import nltk
nltk.download('punkt_tab')
import time # some error easy fix -_-
time.clock = time.time
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__) #obj in flas to create our app in browser



bot = ChatBot("MyChattie", read_only = False,
 logic_adapters  = [
    {
        'import_path':'chatterbot.logic.BestMatch',
        'default_response': 'Nuk e di pergjigjien e kesaj pyetjeje',
        'maximum_similarity_threshhold':0.5 #when to answr in default
        }])

trainer = ChatterBotCorpusTrainer(bot)#
trainer.train('chatterbot.corpus.english')


#url route
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/get') #My get url, very important
def get_chatbot_response():
    request.args.get('userMessage')
#userMessage contains user text in ndex.html
    return str(bot.get_response(userText))
#this response is going to be injected in data in index,html



if __name__ == '__main__':
    app.run(debug =True) #False if published, tregon bugs when run
