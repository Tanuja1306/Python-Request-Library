from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('tasks.db')

# Initialize the database
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database if not already done
init_db()

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        title = data['title']
        description = data['description']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
        conn.close()

        return jsonify({"message": "Task created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()

        task_list = []
        for task in tasks:
            task_dict = {
                'id': task[0],
                'title': task[1],
                'description': task[2]
            }
            task_list.append(task_dict)

        return jsonify({"tasks": task_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()
        conn.close()

        if task:
            task_dict = {
                'id': task[0],
                'title': task[1],
                'description': task[2]
            }
            return jsonify({"task": task_dict})
        else:
            return jsonify({"message": "Task not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update a task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()
        title = data['title']
        description = data['description']

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET title = ?, description = ? WHERE id = ?', (title, description, task_id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Task updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Task deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
