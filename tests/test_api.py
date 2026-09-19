from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_health():
    response = client.get("health")

    assert response.status_code == 200

def test_prediction():
    response = client.post(
        "/predict",
        json={
            "age": 32,
            "income": 75000,
            "previous_purchases": 5,
            "city": "Hyderabad",
            "device": "Mobile"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "purchase_probability" in data