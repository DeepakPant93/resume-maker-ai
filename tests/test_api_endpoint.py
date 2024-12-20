from starlette.testclient import TestClient

from resume_maker_ai.main import app

client = TestClient(app=app)


def test_train_model():
    response = client.post("/api/v1/upload-docs")
    assert response.status_code == 200
    assert response.json() is not None


def test_predict():
    response = client.post("/api/v1/ask")
    assert response.status_code == 200
    assert response.json() is not None
