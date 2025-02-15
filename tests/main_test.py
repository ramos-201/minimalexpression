from starlette.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_homepage():
    response = client.get('/')
    assert response.status_code == 200
