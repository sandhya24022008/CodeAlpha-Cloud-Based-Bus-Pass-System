
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

DATABASE = os.path.join(os.path.dirname(__file__), "bus_pass.db")


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS bus_passes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                phone TEXT NOT NULL,
                route TEXT NOT NULL,
                pass_type TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age_text = request.form.get("age", "").strip()
        phone = request.form.get("phone", "").strip()
        route = request.form.get("route", "").strip()
        pass_type = request.form.get("pass_type", "").strip()

        if not all([name, age_text, phone, route, pass_type]):
            flash("Please fill in all fields.")
            return redirect(url_for("apply"))

        try:
            age = int(age_text)
            if not 1 <= age <= 120:
                raise ValueError
        except ValueError:
            flash("Please enter a valid age.")
            return redirect(url_for("apply"))

        if not phone.isdigit() or len(phone) != 10:
            flash("Enter a valid 10-digit phone number.")
            return redirect(url_for("apply"))

        if pass_type not in ["Daily", "Monthly", "Student"]:
            flash("Please select a valid pass type.")
            return redirect(url_for("apply"))

        with get_db() as db:
            db.execute("""
                INSERT INTO bus_passes
                (name, age, phone, route, pass_type)
                VALUES (?, ?, ?, ?, ?)
            """, (name, age, phone, route, pass_type))

        flash("Application submitted successfully!")
        return redirect(url_for("passes"))

    return render_template("apply.html")


@app.route("/passes")
def passes():
    with get_db() as db:
        records = db.execute(
            "SELECT * FROM bus_passes ORDER BY id DESC"
        ).fetchall()

    return render_template("passes.html", passes=records)


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
  
