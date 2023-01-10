import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()

    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Joao",
            "last_name": "Maria",
            "cpf": "641.396.500-28",
            "email": "joaomaria@gmail.com",
            "birth_date": "1988-12-12"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Jose",
            "last_name": "Yano",
            "cpf": "641.396.500-29",
            "email": "joseyano@gmail.com",
            "birth_date": "1992-09-11"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data
