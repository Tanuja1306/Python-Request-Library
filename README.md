# Python Developer Interview Assignment
This repository contains a Python-based RESTful API for managing tasks. The API allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks, and it integrates with an SQLite database for data persistence. 

# Task Manager REST API

The Task Manager REST API is a Python-based API that provides functionality for managing tasks. It allows users to perform Create, Read, Update, and Delete (CRUD) operations on tasks, and it integrates with an SQLite database for data persistence. This API is built using the Flask framework, adheres to RESTful principles, includes error handling, unit tests.

## Features

- Create a new task with a title and description.
- Retrieve a list of all tasks.
- Retrieve a specific task by its ID.
- Update an existing task by providing the task's ID.
- Delete a task by providing the task's ID.
- SQLite database integration.
- Error handling and status codes.
- Unit tests for API endpoints.
- Clear and concise documentation with example requests and responses.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Pip (Python package manager) installed

### Installation

1. Clone this repository:

2. Create a virtual environment (optional but recommended):


3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

4. Install the required packages:

pip install -r requirements.txt


### Running the API

To run the API, use the following command:

python test.py


The API will start and be accessible at `http://localhost:5000`.

## Usage

To use the API, refer to the API Endpoints section below for details on available routes and request formats.

## API Endpoints

- POST /tasks: Create a new task with a title and description.
- GET /tasks: Retrieve a list of all tasks.
- GET /tasks/{id}: Retrieve a specific task by its ID.
- PUT /tasks/{id}: Update an existing task by providing the task's ID.
- DELETE /tasks/{id}: Delete a task by providing the task's ID.

For detailed information on how to use each endpoint, refer to the API Documentation.

## Testing

To run the unit tests for the API, use the following command:

python test_api.py


## Documentation

Comprehensive documentation on how to use the API, including example requests and responses, can be found in the API Documentation file.

## Contributing

Contributions and improvements to the project are welcome. Please fork the repository, create a new branch, and submit a pull request.

## Author

- Tanuja Kumari
- Email: tanujasangwan@gmail.com
