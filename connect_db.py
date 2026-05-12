import psycopg2

# Your PostgreSQL database details
DB_NAME = "your_database_name"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    connection = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    print("PostgreSQL database connected successfully!")

    cursor = connection.cursor()

    # This only checks connection. It does not insert or update anything.
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()

    print("PostgreSQL Version:")
    print(db_version)

except Exception as e:
    print("Connection failed!")
    print(e)

# finally:
#     if 'cursor' in locals():
#         cursor.close()

#     if 'connection' in locals():
#         connection.close()
#         print("Database connection closed.")