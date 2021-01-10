import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    """
    This is the route for the home page that lists the recipes.
    """
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/")
@app.route("/get_mealplan")
def get_mealplan():
    """
    This is the route for the list of meal plans that have been added to the page .
    """
    mealplan = list(mongo.db.mealplan.find())
    return render_template("mealplan.html", mealplan=mealplan)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This is the route for allowing a user to register
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This is the route for users to be able to log in to the site
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "cooking_steps": request.form.get("cooking_steps"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added!")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/add_mealplan", methods=["GET", "POST"])
def add_mealplan():
    if request.method == "POST":
        mealplan = {
            "category_name": request.form.get("category_name"),
            "mealplan_name": request.form.get("mealplan_name"),
            "mealplan_breakfast": request.form.get("mealplan_breakfast"),
            "mealplan_lunch": request.form.get("mealplan_lunch"),
            "mealplan_dinner": request.form.get("mealplan_dinner"),
            "added_by": session["user"]
        }
        mongo.db.mealplan.insert_one(mealplan)
        flash("Mealplan Added!")
        return redirect(url_for("get_mealplan"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_mealplan.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "cooking_steps": request.form.get("cooking_steps"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/delete_mealplan/<mealplan_id>")
def delete_mealplan(mealplan_id):
    mongo.db.mealplan.remove({"_id": ObjectId(mealplan_id)})
    flash("Mealplan Deleted")
    return redirect(url_for("get_mealplan"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
