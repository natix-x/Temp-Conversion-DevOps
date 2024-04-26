import os
from flask import Flask, request, jsonify

app = Flask(__name__)  # Flask instance creation
app_identifier = os.urandom(24).hex()  # creation of app identifier


def covert_fahrenheit_to_celsius(fahrenheit_temp):
    """
    calculate Celsius temperature based on Fahrenheit temperature
    :param fahrenheit_temp: Fahrenheit temperature
    :return: Celsius temperature
    """
    celsius_temp = (fahrenheit_temp - 32) * (5 / 9)
    return round(celsius_temp, 2)


@app.route("/convert/", methods=["POST"])
def covert_temperature():
    """
    converts Fahrenheit temperature to  Celsius temperature,
    expects JSON formatted data with key: "fahrenheit" containing temperature value (int or float)
    :return: JSON formatted data: if success: Celsius temperature and app identifier randomly
    generated inside the app during startup, if key 'fahrenheit' is missing or temperature value
    has incorrect type: error message
    """
    try:
        data = request.get_json()
        fahrenheit_temperature = data.get("fahrenheit")
        if fahrenheit_temperature is None:
            raise ValueError("Missing 'fahrenheit' value")
        if not isinstance(fahrenheit_temperature, (float, int)):
            raise TypeError("Fahrenheit temperature should be a number")
        celsius_temperature = covert_fahrenheit_to_celsius(fahrenheit_temperature)
        return jsonify({
            "celsius": celsius_temperature,
            "app_identifier": app_identifier
        }), 200
    except (ValueError, TypeError) as e:
        return jsonify({'Error occurred': str(e)}), 400


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
