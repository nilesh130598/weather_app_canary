from flask import Flask, request, jsonify # pyright: ignore[reportMissingImports]
import requests # pyright: ignore[reportMissingModuleSource]
import os
from flask_cors import CORS # type: ignore
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]


app = Flask(__name__)
CORS(app)  # allow frontend to call backend


load_dotenv()
# 🔑 Put your API key here OR use environment variable
API_KEY = os.getenv("API_KEY")

@app.route("/api/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # 🌐 Call OpenWeather API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)

        data = response.json()

        # Handle error from API
        if response.status_code != 200:
            return jsonify(data), response.status_code

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Flask Weather API is running 🚀"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)