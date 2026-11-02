from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect("apartment.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/residents", methods=["GET", "POST"])
def residents():

    connection = get_db_connection()

    if request.method == "POST":
        name = request.form["name"]
        apartment = request.form["apartment"]
        phone = request.form["phone"]

        connection.execute(
            "INSERT INTO residents (name, apartment_number, phone) VALUES (?, ?, ?)",
            (name, apartment, phone)
        )

        connection.commit()
        connection.close()

        return redirect("/residents")

    resident_list = connection.execute(
        "SELECT * FROM residents"
    ).fetchall()

    connection.close()

    return render_template(
        "residents.html",
        residents=resident_list
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
