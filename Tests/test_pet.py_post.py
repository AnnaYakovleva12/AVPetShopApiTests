import allure
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature("Pet")
class TestPet:

    @allure.title("Создание нового питомца (POST /pet)")
    def test_create_pet(self):

        with allure.step("Подготовка тела запроса"):
            payload = {
                "id": 10001,
                "name": "Barsik",
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

            assert body["id"] == 10001
            assert body["name"] == "Barsik"
            assert body["status"] == "available"