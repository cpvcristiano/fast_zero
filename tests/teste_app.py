from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organização)

    response = client.get('/')  # Act(Ação)

    assert response.status_code == HTTPStatus.OK  # assert
    assert response. response.json() == {'massege': 'Olá otario'}  # Asset

    ...
