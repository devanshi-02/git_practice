# routes.py
from flask import jsonify, request


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "message": "Flask GitHub Practice API is running!"
        })

    @app.route("/hello/<name>", methods=["GET"])
    def hello(name):
        return jsonify({
            "message": f"Hello, {name}!"
        })

    @app.route("/add", methods=["POST"])
    def add_numbers():
        data = request.get_json()

        num1 = data.get("num1", 0)
        num2 = data.get("num2", 0)

        result = num1 + num2

        return jsonify({
            "num1": num1,
            "num2": num2,
            "result": result
        })

    @app.route("/status", methods=["GET"])
    def status():
        return jsonify({
            "status": "success",
            "server": "running"
        })