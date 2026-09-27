from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Yah!! Task Management API is Running!!"
    }

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Created by pytest",
            "completed": False
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "Created by pytest"
    assert response.json()["completed"] is False

def test_get_task():
    response = client.get("/tasks")

    assert response.status_code ==200
    assert isinstance(response.json(),list)

def test_get_tasks():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_update_task():
    response = client.put(
        "/tasks/1",
        json={
            "title": "Updated Test Task",
            "description": "Updated by pytest",
            "completed": True
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Task"
    assert response.json()["description"] == "Updated by pytest"
    assert response.json()["completed"] is True

"""def test_delete_task():
    response = client.delete("/tasks/5")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task deleted successfully"
    }"""

def test_delete_task():
    create_response = client.post(
        "/tasks",
        json={
            "title": "Tsask for delete test",
            "description": "This task will be deleted",
            "completed": False
        }

    )

    task_id = create_response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Task deleted successfully"
    }

def test_get_task_not_found():
    response = client.get("/tasks/9999")

    assert response.status_code == 404
    assert response.json() == {
        "detail" : "Task not found"
    }

def test_create_task_validation_error():
    response = client.post(
        "/tasks", 
        json={
            "description": "Title is missing",
            "completed": False
        }
    )

    assert response.status_code == 422
