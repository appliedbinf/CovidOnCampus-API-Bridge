import os
from flask import Flask, make_response, request, jsonify
from requests import post
api_slug = os.environ.get('API_SLUG')
api_key = os.environ.get('API_KEY')
app = Flask(__name__)

@app.route("/1a3d938fa25141aa915b2d7146a14877", methods=['POST'])
def api():
	content = request.get_json(force=True)
	post(f"https://covid19.biosci.gatech.edu/api/v1/{api_slug}", json=content, headers= {'api_key': api_key})
	return make_response("ok", 200)

@app.route('/ping/', methods=['GET'])
def ping():
	return make_response("pong", 200)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
