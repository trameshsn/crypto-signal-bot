import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "🚀 Crypto Signal Bot is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))