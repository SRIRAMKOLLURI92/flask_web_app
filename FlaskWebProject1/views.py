"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/final')
def final():
    """Renders the final page."""
    return render_template(
        'final.html',
        title='Final',
        year=datetime.now().year,
        message='Your final page.'
    )


@app.route('/final')
def devops():
    """Renders the final page."""
    return render_template(
        'final.html',
        title='Final',
        year=datetime.now().year,
        message='My name is SRIRAMKOLLURI - 02-12-2025 '
    )
