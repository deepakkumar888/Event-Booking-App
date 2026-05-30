from flask import Flask, render_template, request

app = Flask(__name__)

events = [
    {
        "name": "Music Concert",
        "date": "20 May 2026",
        "location": "Delhi",
        "description": "Enjoy live music performances by popular artists.",
        "image": "concert.jpg",
        "category": "Music"
    },
    {
        "name": "Tech Seminar",
        "date": "25 May 2026",
        "location": "Chandigarh",
        "description": "Learn about latest technologies and innovations.",
        "image": "tech.jpg",
        "category": "Technology"
    },
    {
        "name": "Wedding Expo",
        "date": "30 May 2026",
        "location": "Ludhiana",
        "description": "Explore wedding planning ideas and services.",
        "image": "wedding.jpg",
        "category": "Wedding"
    },
    {
        "name": "Dandiya Night",
        "date": "5 June 2026",
        "location": "Ahmedabad",
        "description": "Celebrate Navratri with music, dance, and fun.",
        "image": "dandiya.jpg",
        "category": "Cultural"
    },
    {
        "name": "Stand-Up Comedy Show",
        "date": "10 June 2026",
        "location": "Mumbai",
        "description": "Enjoy an evening full of laughter and entertainment.",
        "image": "comedy.jpg",
        "category": "Entertainment"
    },
    {
        "name": "Food Festival",
        "date": "15 June 2026",
        "location": "Amritsar",
        "description": "Taste delicious dishes and explore food stalls.",
        "image": "food.jpg",
        "category": "Food"
    }
]

bookings = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    return render_template(
        'index.html',
        events=events,
        username=username
    )

@app.route('/book', methods=['POST'])
def book_event():

    username = request.form['username']
    event_name = request.form['event_name']

    bookings.append({
        "username": username,
        "event": event_name
    })

    return render_template(
        'success.html',
        username=username,
        event=event_name
    )

@app.route('/bookings')
def view_bookings():

    return render_template(
        'bookings.html',
        bookings=bookings
    )

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000
    )