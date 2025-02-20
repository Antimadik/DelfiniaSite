from flask import Flask, render_template, request, redirect, url_for, flash, session
import json
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Проверка допустимых расширений файлов
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница с правилами сервера
@app.route('/rules')
def rules():
    return render_template('rules.html')

# Обработчик ошибки 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
