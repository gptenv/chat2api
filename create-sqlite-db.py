import sqlite3

# Path to the database file (you can modify this to any path you want)
db_path = './data/session_storage.db'  # Relative path for local use (default location)

# Connect to the SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect(db_path)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the sessions table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        req_token TEXT PRIMARY KEY,
        conversation_id TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

