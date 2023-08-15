from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a database connection
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        content TEXT
    )
''')
conn.commit()

@app.route('/send_message', methods=['POST'])
def send_message():
    content = request.json.get('content')
    if content:
        cursor.execute('INSERT INTO messages (content) VALUES (?)', (content,))
        conn.commit()
        return jsonify({'message': 'Message sent successfully'}), 201
    else:
        return jsonify({'error': 'Content is required'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    cursor.execute('SELECT * FROM messages')
    messages = [{'id': row[0], 'content': row[1]} for row in cursor.fetchall()]
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)
