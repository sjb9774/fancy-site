from fancy_site import app
from flask import render_template

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
