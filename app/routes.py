from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anderson'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avenger movies was so cool!'
        },
        {
            'author': {'username': 'Guillermo'},
            'body': 'I going to be on of the best python developers from El Salvador.'
        },
        {
            'author': {'username': 'Laura'},
            'body': 'I love to service to my God!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    