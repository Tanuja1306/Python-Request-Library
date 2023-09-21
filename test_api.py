import unittest
import json
from app import app

class TaskManagerAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_task(self):
        task_data = {
            'title': 'Task 1',
            'description': 'This is the first task.'
        }
        response = self.app.post('/tasks', json=task_data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', data)
        self.assertEqual(data['title'], 'Task 1')
        self.assertEqual(data['description'], 'This is the first task.')

    def test_get_all_tasks(self):
        response = self.app.get('/tasks')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_task_by_id(self):
        # Create a task first
        task_data = {
            'title': 'Task 2',
            'description': 'This is the second task.'
        }
        response = self.app.post('/tasks', json=task_data)
        data = json.loads(response.data)
        task_id = data['id']

        # Retrieve the task by ID
        response = self.app.get(f'/tasks/{task_id}')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Task 2')
        self.assertEqual(data['description'], 'This is the second task.')

    def test_update_task(self):
        # Create a task first
        task_data = {
            'title': 'Task 3',
            'description': 'This is the third task.'
        }
        response = self.app.post('/tasks', json=task_data)
        data = json.loads(response.data)
        task_id = data['id']

        # Update the task
        updated_data = {
            'title': 'Updated Task 3',
            'description': 'This is the updated third task.'
        }
        response = self.app.put(f'/tasks/{task_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)

        # Retrieve the updated task
        response = self.app.get(f'/tasks/{task_id}')
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated Task 3')
        self.assertEqual(data['description'], 'This is the updated third task.')

    def test_delete_task(self):
        # Create a task first
        task_data = {
            'title': 'Task 4',
            'description': 'This is the fourth task.'
        }
        response = self.app.post('/tasks', json=task_data)
        data = json.loads(response.data)
        task_id = data['id']

        # Delete the task
        response = self.app.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 204)

        # Attempt to retrieve the deleted task
        response = self.app.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
