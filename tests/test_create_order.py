import allure
import pytest
import requests
import data

class TestCreateOrder:
    @allure.title('Тест на создание заказа с авторизацией с ингредиентами, без ингредиентов и с неверным хешем ингредиентов, ручка: /api/orders')
    @pytest.mark.parametrize('registration_data, expected_status_code', data.OrderIngredients.create_order_variants)
    def test_create_order_with_login_user(self, registration_data, expected_status_code, create_duplicate_user):
        requests.post(f'{data.Url.LOGIN_USER}', json=create_duplicate_user)
        payload = {'ingredients': registration_data}
        response = requests.post(f'{data.Url.CREATE_ORDER}', json=payload)
        response_body = response.json()
        response.status_code = expected_status_code

        if expected_status_code == 200:
            assert response_body['success'] is True
            assert 'name' in response_body.keys()
            assert 'number' in response_body['order'].keys()

        elif expected_status_code == 400:
            assert response_body['success'] is False
            assert 'message' in response_body.keys()
            assert response_body['message'] == "Ingredient ids must be provided"

        elif expected_status_code == 500:
            assert response.status_code == 500

    @allure.title('Тест на создание заказа без авторизации с ингредиентами, без ингредиентов и с неверным хешем ингредиентов, ручка: /api/orders')
    @pytest.mark.parametrize('registration_data, expected_status_code', data.OrderIngredients.create_order_variants)
    def test_create_order_without_login_user(self, registration_data, expected_status_code):
        payload = {'ingredients': registration_data}
        response = requests.post(f'{data.Url.CREATE_ORDER}', json=payload)
        response_body = response.json()
        response.status_code = expected_status_code

        if expected_status_code == 200:
            assert response_body['success'] is True
            assert 'name' in response_body.keys()
            assert 'number' in response_body['order'].keys()

        elif expected_status_code == 400:
            assert response_body['success'] is False
            assert 'message' in response_body.keys()
            assert response_body['message'] == "Ingredient ids must be provided"

        elif expected_status_code == 500:
            assert response.status_code == 500

