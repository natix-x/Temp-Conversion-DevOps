from locust import HttpUser, task, between


class User(HttpUser):
    wait_time = between(1, 2)

    @task
    def convert_temperature(self):
        payload = {"fahrenheit": 32}
        self.client.post("/v1/models/tensorflow_model:predict", json=payload)
