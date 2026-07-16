from flask import Flask, render_template

app = Flask(__name__)

products = [
    {
        "name": "Gaming Laptop",
        "price": "₹65,000",
        "image": "https://via.placeholder.com/250x180?text=Laptop"
    },
    {
        "name": "Smartphone",
        "price": "₹30,000",
        "image": "https://via.placeholder.com/250x180?text=Phone"
    },
    {
        "name": "Wireless Headphones",
        "price": "₹2,500",
        "image": "https://via.placeholder.com/250x180?text=Headphones"
    },
    {
        "name": "Mechanical Keyboard",
        "price": "₹1,500",
        "image": "https://via.placeholder.com/250x180?text=Keyboard"
    }
]

@app.route("/")
def home():
    return render_template("products.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
