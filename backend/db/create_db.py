import sqlite3
def create(db_name):
    conn = sqlite3.connect("database.db")
    cursor=conn.cursor()

    cursor.execute('''
        CREATE TABLE MarketData (
            date DATE NOT NULL,
            product.id INTEGER REFERENCES Product(id),
            price NUMERIC(10, 2),
            sales_volume INTEGER
        )

    ''')
    cursor.execute('''
        CREATE TABLE Forecast (
            id SERIAL PRIMARY KEY,
            product_id INTEGER REFERENCES Product(id),
            forecast_date DATE NOT NULL,
            predicted_sales INTEGER
    ''')

    cursor.execute('''
        CREATE TABLE Product (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(100),
            description TEXT
    ''')