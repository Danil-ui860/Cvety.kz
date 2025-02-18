from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Ключ для сессии

# Товары
products = [
    {"id": 1, "title": "Теона", "price": 6000, "img": "img/1.webp"},
    {"id": 2, "title": "Роза", "price": 5500, "img": "img/2.webp"},
    {"id": 3, "title": "Лилия", "price": 3000, "img": "img/3.webp"}
]

# Главная страница
@app.route("/")
def index():
    return render_template("index.html", products=products)

# Добавить товар в корзину
@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    
    for product in products:
        if product["id"] == product_id:
            session["cart"].append(product)
            session.modified = True
            break

    return redirect(url_for("cart"))

# Показать корзину
@app.route("/cart")
def cart():
    cart_items = session.get("cart", [])
    return render_template("cart.html", cart_items=cart_items)

# Удалить товар из корзины
@app.route("/remove_from_cart/<int:index>")
def remove_from_cart(index):
    if "cart" in session and index < len(session["cart"]):
        session["cart"].pop(index)
        session.modified = True
    return redirect(url_for("cart"))

# Очистить корзину
@app.route("/clear_cart")
def clear_cart():
    session["cart"] = []
    session.modified = True
    return redirect(url_for("cart"))

if __name__ == "__main__":
    app.run(debug=True)


