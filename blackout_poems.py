import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diamnonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diamvoluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clitakasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Loremipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmodtempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasdgubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."   


@app.route('/')
def index():
    text_list = text.strip().split()
    random_items = []
    for x in range(7):
        random_items.append(random.choice([i for i,j in enumerate(text_list)]))

    return render_template('index.html', text=enumerate(text_list),
                           random_items=random_items)
