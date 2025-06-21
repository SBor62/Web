from flask import Flask, render_template_string, request  # Исправленный импорт

app = Flask(__name__)

# HTML-шаблон с формой и отображением данных
template = '''
<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Анкета пользователя</title>
</head>
<body>
    <h1>Заполните анкету</h1>
    <form method="POST">
        <label>Имя:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Город:</label><br>
        <input type="text" name="city" required><br><br>

        <label>Хобби:</label><br>
        <input type="text" name="hobby" required><br><br>

        <label>Возраст:</label><br>
        <input type="number" name="age" min="0" required><br><br>

        <button type="submit">Отправить</button>
    </form>

    {% if submitted %}
        <h2>Введённые данные:</h2>
        <p><strong>Имя:</strong> {{ data.name }}</p>
        <p><strong>Город:</strong> {{ data.city }}</p>
        <p><strong>Хобби:</strong> {{ data.hobby }}</p>
        <p><strong>Возраст:</strong> {{ data.age }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получение данных из формы
        data = {
            'name': request.form.get('name', ''),
            'city': request.form.get('city', ''),
            'hobby': request.form.get('hobby', ''),
            'age': request.form.get('age', '')
        }
        return render_template_string(template, submitted=True, data=data)
    return render_template_string(template, submitted=False)


if __name__ == '__main__':
    app.run(debug=True)
