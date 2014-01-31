import random
import requests
import re
import datetime
import os
import cPickle as pickle
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


def post_von_wagner():
    ''' check if pickle file is already there, else get it '''
    today = datetime.date.today().isoformat()

    if os.path.exists(today+'.p'):
        temp_file = open(today+'.p', 'rb')
        trash = pickle.load(temp_file)

    else:
        temp_file = open(today+'.p', 'wb+')

        ''' get the link to the newest post'''
        URL = "http://www.bild.de/themen/personen/franz-josef-wagner/kolumne-17304844.bild.html"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text)
        URL = 'http://www.bild.de'+soup.find('div', 'tr').find('a').get('href')

        ''' get the text out the article '''
        r = requests.get(URL)
        soup = BeautifulSoup(r.text)
        trash = soup.find('div', 'txt clearfix').text

        ''' clean everything up and create a list'''
        trash = re.sub(r'[\;\,\(\).\"\@\:\?]', ' ', trash)
        trash = trash.split()

        ''' save trash to pickle file '''
        pickle.dump(trash, temp_file)

    temp_file.close()
    return trash[:-24]


@app.route('/')
def index():
    text = post_von_wagner()
    random_items = []
    for x in range(7):
        random_items.append(random.choice([i for i, j in enumerate(text)]))

    return render_template('index.html', text=enumerate(text),
                           random_items=random_items)
