from flask import Flask

app = Flask(__name__)

@app.route('/')
def admin_home():
    return """
    <h1>Admin Dashboard</h1>
    <h3>Event Booking Management System</h3>
    <p>Running on Port 5001</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)