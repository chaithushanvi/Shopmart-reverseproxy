from flask import Flask, render_template

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@gmail.com",
        "role": "Customer"
    },
    {
        "id": 2,
        "name": "Alice Smith",
        "email": "alice@gmail.com",
        "role": "Seller"
    },
    {
        "id": 3,
        "name": "Robert Brown",
        "email": "robert@gmail.com",
        "role": "Customer"
    }
]

@app.route("/")
def home():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
