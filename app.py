from flask import Flask, jsonify

app = Flask(__name__)

movies = [
    {
        "title": "John Wick 4",
        "poster": "https://yourcdn.com/johnwick.jpg",
        "stream_url": "https://yourcdn.com/johnwick4.m3u8"
    },
    {
        "title": "Avengers: Endgame",
        "poster": "https://yourcdn.com/endgame.jpg",
        "stream_url": "https://yourcdn.com/endgame.m3u8"
    }
]

@app.route('/')
def home():
    return "Movie API is Live 🎬"

@app.route('/movies')
def get_movies():
    return jsonify(movies)

if __name__ == "__main__":
    app.run()
