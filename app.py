from flask import Flask, jsonify
import json
import os


app = Flask(__name__)
app_dir = os.path.dirname(os.path.abspath(__file__))

@app.route("/api")
def api():
    try:
        
        file_path = os.path.join(app_dir, "data.json")
        
        with open(file_path, "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
