# connect fromtend with main.py

from flask import Flask, request, jsonify
from main import get_recommendation

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_id = data['user_id']
    recommended = get_recommendation(user_id)
    return jsonify({'recommended': recommended})

if __name__ == '__main__':
    app.run(port=5000)