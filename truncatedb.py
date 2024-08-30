import mysql.connector
from mysql.connector import Error

# Establishing a connection to MySQL
connection = None

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Update if your MySQL root user has a password
        port=3307     # Default MySQL port; update if necessary
    )

    if connection.is_connected():
        print("Connected to MySQL Server")

        # Creating a cursor object
        cursor = connection.cursor()

        # Selecting the database
        cursor.execute("USE dummy_database")

        # Getting the list of tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Truncating each table
        for (table_name,) in tables:
            cursor.execute(f"TRUNCATE TABLE {table_name}")
            print(f"Table {table_name} truncated successfully")

        # Dropping the database
        cursor.execute("DROP DATABASE dummy_database")
        print("Database 'dummy_database' deleted successfully")

        connection.commit()

except Error as e:
    print(f"Error: {e}")
finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
