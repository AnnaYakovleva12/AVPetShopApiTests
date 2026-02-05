import allure
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature("Pet")
class TestPet:

    @allure.title("Создание нового питомца (POST /pet)")
    def test_create_pet(self):

        with allure.step("Подготовка тела запроса"):
            payload = {
                "id": 10002,
                "name": "Bars",
                "category": {
                    "id": 1,
                    "name": "Cats"
                },
                "photoUrls": [
                    "https://example.com/cat.jpg"
                ],
                "tags": [
                    {
                        "id": 1,
                        "name": "home"
                    }
                ],
                "status": "available"
            }

        with allure.step("Отправка POST запроса"):
            response = requests.post(
                url=f"{BASE_URL}/pet",
                json=payload
            )

        with allure.step("Проверка статус кода"):
            assert response.status_code == 200

        with allure.step("Проверка данных питомца в ответе"):
            body = response.json()
            pet_id = body["id"]

            assert body["id"] == 10002
            assert body["name"] == "Bars"
            assert body["status"] == "available"

            with allure.step("Удаляем созданного питомца"):
                delete_response = requests.delete(
                    url=f"{BASE_URL}/pet/{pet_id}"
                )

                assert delete_response.status_code == 200

            with allure.step("Проверяем что питомец удалён"):
                get_response = requests.get(
                    url=f"{BASE_URL}/pet/{pet_id}"
                )

                assert get_response.status_code == 404