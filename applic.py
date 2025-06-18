from flask import Flask, render_template

applic = Flask(__name__)

@applic.route('/')
def index():
    return render_template('index.html', title='Главная')

@applic.route('/blog')
def blog():
    return render_template('blog.html', title='Блог')

@applic.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')

if __name__ == '__main__':
    applic.run(debug=True)
