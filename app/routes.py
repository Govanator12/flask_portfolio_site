from app import app
from flask import render_template, url_for, redirect, flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/experience')
def experience():
    return render_template('experience.html', title='Experience')


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
