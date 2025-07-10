from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def service_b():
    # This message is different to distinguish it from Service A
    return "Hello from Service B!\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
