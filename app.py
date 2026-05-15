#file is for calling end points
# app.py

from flask import Flask, jsonify, request
from routes import register_routes

app = Flask(__name__)

# Register all routes from another file
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)