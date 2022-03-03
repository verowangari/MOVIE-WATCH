from flask import render_template
from app import app
#views function
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html') #Takes in the name of a template file as the first argument
