from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Laptop Controller API Running"
    })

@app.route("/open-notepad")
def open_notepad():
    os.system("notepad")
    return jsonify({
        "status": "Notepad Opened"
    })

@app.route("/shutdown")
def shutdown():
    os.system("shutdown /s /t 30")
    return jsonify({"status": "Shutdown in 30 seconds"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
@app.route("/open-chrome")
def open_chrome():
    os.system("start chrome")
    return jsonify({"status": "Chrome Opened"})

@app.route("/lock")
def lock():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return jsonify({"status": "Laptop Locked"})
