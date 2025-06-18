from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_current_time():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Текущие дата и время</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }}
            h1 {{ color: #333; }}
            .time {{ font-size: 24px; color: #0066cc; }}
        </style>
        <script>
            function updateTime() {{
                fetch('/time')
                    .then(response => response.json())
                    .then(data => {{
                        document.getElementById('time').textContent = data.time;
                    }});
            }}
            setInterval(updateTime, 1000);
        </script>
    </head>
    <body>
        <h1>Текущие дата и время:</h1>
        <div id="time" class="time">{current_time}</div>
    </body>
    </html>
    """

@app.route('/time')
def get_time():
    return jsonify({'time': datetime.now().strftime("%d.%m.%Y %H:%M:%S")})

if __name__ == '__main__':
    app.run(debug=True)
