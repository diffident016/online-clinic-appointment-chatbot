from flask import Flask, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index():
	return "<p>Server is running...</p>"

@app.post("/predict")
def predict():
	text = request.get_json().get("message")
	response = get_response(text)
	message = {"answer" : response}
	return jsonify(message)

if __name__ == "__main__":
	app.run(host= "0.0.0.0", port= 5000)