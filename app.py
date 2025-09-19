from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>My Python CI/CD App</h1>
    <p>Version: 1.0.0</p>
    <p>Status: Running successfully!</p>
    <p>Current time: {}</p>
    <a href="/api/health">Health Check</a> | 
    <a href="/api/users">View Users</a>
    '''.format(datetime.now())

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/users')
def users():
    return jsonify([
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
    ])

@app.route('/api/calculate/<int:num>')
def calculate(num):
    return jsonify({
        'number': num,
        'square': num * num,
        'cube': num * num * num
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)