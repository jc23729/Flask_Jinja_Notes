from flask import flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)


"""You want to setup a template directory, a folder where your going to have repeatable code
my-project-directory/
  venv/
  app.py
  templates/
    hello.html
"""
@app.route ('/hello')
def say_hello():
    """shows hello page and will look for file hello.html"""
    return render_template("hello.html")


## JINJA VARIABLES 

# Ex  of file         templates/lucky.html

# Jinja will replace things like {{ msg }} with value of msg passed when rendering:

# Ex of file                 app.py 
# @app.route("/lucky")
# def show_lucky_num():
#     "Example of simple dynamic template"

#     num = randint(1, 100)

#     return render_template("lucky.html",
#                           lucky_num=num)

@app.route("/lucky")
def show_lucky_num():
    "Example of simple dynamic template"
    num = randint(1,10)
    return render_template("lucky.html", lucky_num =num, msg="You are so lucky!")


  ####JINJA Conditionals 
#used in html template
  {% if CONDITION_EXPR %} ... {% endif %}

{% if compliments %}
  You're so:
  ...
{% endif %}


#JINJA LOOPS


@app.route('/spell/<word>')
def spell_word(word):
  return render_template('spell_word.html', word = word)


@app.route('/form-2')
def show_form_2():
  return render_template("form_2.html")

@app.route('/greet-2')
def get_greeting_2():
  