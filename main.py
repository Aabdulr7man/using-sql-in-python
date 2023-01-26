import sqlite3


def create_faq_table():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS 'faq' (text TEXT)")
    conn.commit()


def create_data_table():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS 'data' (name VARCHAR (30) PRIMARY KEY NOT NULL,address VARCHAR (255) NOT NULL,bio VARCHAR (255) ")
    conn.commit()

def insert_faq_data(mytext):
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute(''' INSERT INTO faq (text) VALUES (mytext) ''')
    conn.commit()

    def data_table_insert(name, address, bio):
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute(''' INSERT INTO data (name, address, bio) VALUES (name, address, bio) ''')
    conn.commit()
