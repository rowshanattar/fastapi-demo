from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_add():
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"total": 5}