from flask import render_template
from . import  app

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

