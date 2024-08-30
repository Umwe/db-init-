import mysql.connector
from mysql.connector import Error

# Establishing a connection to MySQL
connection = None

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Update if your MySQL root user has a password
        port=3307     # Default mostly #3306
    )


    
    if connection.is_connected():
        print("Connected to MySQL Server")

        # Creating a cursor object
        cursor = connection.cursor()

        # Creating a database
        cursor.execute("CREATE DATABASE IF NOT EXISTS dummy_database")
        print("Database created successfully")

        # Selecting the database
        cursor.execute("USE dummy_database")

        # Creating a table with 5 columns
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dummy_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            email VARCHAR(255),
            country VARCHAR(255),
            registration_date DATE
        )
        """)
        print("Table created successfully")

        # Inserting 10 dummy rows of data
        cursor.executemany("""
        INSERT INTO dummy_table (name, age, email, country, registration_date)
        VALUES (%s, %s, %s, %s, %s)
        """, [
            ('John Doe', 28, 'john@example.com', 'USA', '2024-01-01'),
            ('Jane Smith', 34, 'jane@example.com', 'UK', '2024-02-01'),
            ('Alice Johnson', 29, 'alice@example.com', 'Canada', '2024-03-01'),
            ('Bob Brown', 41, 'bob@example.com', 'Australia', '2024-04-01'),
            ('Charlie Davis', 22, 'charlie@example.com', 'USA', '2024-05-01'),
            ('Eva Green', 30, 'eva@example.com', 'Germany', '2024-06-01'),
            ('Frank White', 27, 'frank@example.com', 'France', '2024-07-01'),
            ('Grace Lee', 35, 'grace@example.com', 'Japan', '2024-08-01'),
            ('Henry Walker', 40, 'henry@example.com', 'China', '2024-09-01'),
            ('Ivy Harris', 26, 'ivy@example.com', 'Brazil', '2024-10-01')
        ])
        connection.commit()
        print("Inserted 10 rows of data successfully")

except Error as e:
    print(f"Error: {e}")
finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
