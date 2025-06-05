from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_back_project.app import app


def test_read_root_retorna_ok_e_ola_mundo():
    client = TestClient(app)  # arrange
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Olá mundo!'}
