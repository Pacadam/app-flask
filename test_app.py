import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bonjour' in response.data


def test_sante(client):
    response = client.get('/sante')
    assert response.status_code == 200
    assert response.data == b'OK'


def test_route_inexistante(client):
    response = client.get('/cette-route-nexiste-pas')
    assert response.status_code == 404
