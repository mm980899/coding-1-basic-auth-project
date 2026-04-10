import sqlite3

def get_db2():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db2():
    conn = get_db2()
    # Add your new table between lines 15 & 16.
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT PRIMARY KEY,
            user TEXT,
            open TEXT
        )
    """)
    conn.commit()
    conn.close()