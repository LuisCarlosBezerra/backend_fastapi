from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_back_project.app import app


def test_read_root_retorna_ok_e_ola_mundo():
    client = TestClient(app)  # arrange
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá mundo!'}


def test_read_root_retorna_ok_e_ola_mundo_html():
    client = TestClient(app)
    response = client.get('/html_message')
    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá mundo!</h1>' in response.text
