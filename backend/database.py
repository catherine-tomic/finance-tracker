import sqlite3

def create_db():
    connection = sqlite3.connect('finance-tracker.db')
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS transactions')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        date TEXT,
        amount REAL,
        category TEXT,
        description TEXT
    )
    ''')

    connection.commit()
    connection.close()

def addTestValue1():
    connection = sqlite3.connect('finance-tracker.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO transactions (date, amount, category, description)
    VALUES ('2025-03-25', 10.35, 'Food', 'Lunch in Alexandria')
    ''')

    connection.commit()

    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()

if __name__ == "__main__":
    create_db()
    addTestValue1()