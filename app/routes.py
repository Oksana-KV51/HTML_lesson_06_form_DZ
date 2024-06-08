from flask import render_template, request, redirect, url_for
from app import app

# Хранилище для данных пользователей
users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global users
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Добавление данных пользователя в список
        users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})

    return render_template('blog.html', users=users)
