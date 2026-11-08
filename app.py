#import needed libraries
from flask import Flask
import sqlite3
import os

app = Flask(__name__)

#Database files location and database is saved to the same folder where this app.py
DATABASE = os.path.join(os.path.dirname(__file__), "visitors.db")

#open connection
def get_db():
    return sqlite3.connect(DATABASE)
#making visitor table
def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS visitors (
                id INTEGER PRIMARY KEY,
                count INTEGER NOT NULL
            )
        """)

        db.execute("""
            INSERT OR IGNORE INTO visitors (id, count)
            VALUES (1, 0)
        """)
  @app.route("/")
def home():
    with get_db() as db:
        db.execute("""
            UPDATE visitors
            SET count = count + 1
            WHERE id = 1
        """)

        result = db.execute("""
            SELECT count FROM visitors WHERE id = 1
        """).fetchone()

    visitor_count = result[0]
  #visitor page shown to user with total visitor counter.
  return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Week 2 assignment</title>
        <style>
            body {{
                background: #171717;
                color: #f5f5f5;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 60px 20px;
            }}
            .container {{
                max-width: 650px;
                margin: auto;
                padding: 35px;
                background: #262626;
                border: 1px solid #404040;
                border-radius: 12px;
            }}
      h1, h2 {{
                color: #f97316;
            }}
            .count {{
                font-size: 60px;
                color: #fb923c;
                font-weight: bold;
                margin: 20px;
            }}
            p {{
                color: #d4d4d4;
                line-height: 1.7;
            }}
            a {{
                color: #fb923c;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Week 2 - Python application and database</h1>

            <h2>Total visits</h2>

             <div class="count">{visitor_count}</div>


            <h2>Database and counter</h2>

            <p>
                I used SQLite for database, because i was already familiar with it. it stores total time visted in
                site in visitors.db
            </p>

        </div>
    </body>
    </html>
    """
if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000)
