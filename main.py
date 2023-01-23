import sqlite3


def create_faq_table():
    conn = sqlite3.connect('mydb.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS 'faq' (text TEXT)")


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
