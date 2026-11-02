
import sqlite3

def create_database():
    connection = sqlite3.connect("apartment.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS residents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            apartment_number TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database created successfully!")

create_database()
