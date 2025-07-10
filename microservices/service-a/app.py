from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def service_a():
    return "Hello from Service A!\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
