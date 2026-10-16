import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "bloodbank.db")


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    bloodbanks = []

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if city:
            conn = get_db_connection()
            c = conn.cursor()
            # Case-insensitive partial match on city name
            c.execute(
                "SELECT * FROM bloodbanks WHERE city LIKE ?",
                (f"%{city}%",)
            )
            bloodbanks = c.fetchall()
            conn.close()

    return render_template(
        "index.html",
        bloodbanks=bloodbanks
    )


if __name__ == "__main__":
    app.run(debug=True)
