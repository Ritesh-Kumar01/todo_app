import sqlite3

def get_connection():
    return sqlite3.connect("todo.db")

con = get_connection()

cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS todo (
    todoID INTEGER PRIMARY KEY,
    todo_name TEXT NOT NULL,
    todo_desc TEXT,
    created_at DATE DEFAULT CURRENT_DATE,
    status TEXT DEFAULT 'Not Completed'
)
""")
con.commit()


