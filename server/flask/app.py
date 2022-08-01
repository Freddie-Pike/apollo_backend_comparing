from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_users")
def get_users():
    userData = [
        {"username": "user1", "email": "user1@example.com"},
        {"username": "user222", "email": "user2@example.com"},
    ]
    return jsonify(userData)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
