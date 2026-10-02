# Task Management API

A RESTful Task Management API built with Python, FastAPI, SQLAlchemy, and PostgreSQL.

## Features

* Create, read, update, and delete tasks
* PostgreSQL database integration
* RESTful API endpoints
* Request validation with Pydantic
* API error handling with appropriate HTTP status codes
* Automated API testing with pytest
* Interactive API documentation with Swagger UI

## Technologies

* **Language:** Python
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Database:** PostgreSQL
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Testing:** pytest
* **Environment Management:** python-dotenv

## Project Structure

```text
task-management-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   └── test_main.py
│
├── requirements.txt
└── README.md
```

> Note: The `.env` file is used for local environment configuration and is not included in the repository.

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root and add your database connection string:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/task_management_db
```

Replace `username` and `password` with your local PostgreSQL credentials.

> Never commit the `.env` file to the repository because it may contain sensitive credentials.

## Run the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Interactive API documentation is available through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to view the available endpoints and send API requests directly from the browser.

## API Endpoints

| Method | Endpoint           | Description               |
| ------ | ------------------ | ------------------------- |
| GET    | `/`                | Check API status          |
| POST   | `/tasks`           | Create a new task         |
| GET    | `/tasks`           | Get all tasks             |
| GET    | `/tasks/{task_id}` | Get a single task         |
| PUT    | `/tasks/{task_id}` | Update a task             |
| DELETE | `/tasks/{task_id}` | Delete a task             |
| GET    | `/db-test`         | Check database connection |

## Testing

The project includes automated API tests using pytest.

Run all tests with:

```bash
pytest
```

The test suite covers:

* Root endpoint
* Task creation
* Get all tasks
* Get a single task
* Task update
* Task deletion
* 404 error handling
* Request validation
