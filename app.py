from flask import flask, request, render_template

app = Flask(__name__)


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