from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task # noqa


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = request.form.get("category_name")
        new_category = Category(category_name=category)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
