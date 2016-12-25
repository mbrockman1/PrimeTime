import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def prime(number):
    return not (number < 2 or
                any(number % x == 0
                    for x in range(2, int(number ** 0.5) + 1)))


@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("YesIntent")
def number_asker():
    ask_for_number_msg = render_template('ask_for_number')
    return question(ask_for_number_msg)


@ask.intent("AnswerIntent", convert={'the_input': int})
def is_it_prime(the_input):
    # winning_numbers = session.attributes['numbers']
    is_prime = prime(the_input)
    if is_prime:
        msg = render_template('prime')
    else:
        msg = render_template('not_prime')
    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)
