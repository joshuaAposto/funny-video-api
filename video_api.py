from flask import Flask, jsonify, request
import json

app = Flask(__name__)


with open('videos.json', 'r') as f:
    videos = json.load(f)


@app.route('/videos', methods=['GET'])
def get_videos():
    return jsonify(videos)
    
    
@app.route('/videos', methods=['POST'])
def add_video():
    new_video = request.json
    videos.append(new_video)
    with open('videos.json', 'w') as f:
        json.dump(videos, f, indent=4)
    return jsonify(new_video), 201

if __name__ == '__main__':
    app.run(debug=True)
