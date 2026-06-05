import os
import sys
import psycopg2
import time

print("Starting application...", flush=True)

db_host = os.getenv("DB_HOST", "postgres_db")
db_user = os.getenv("DB_USER", "myuser")
db_password = os.getenv("DB_PASSWORD", "mypassword")
db_name = os.getenv("DB_NAME", "mydb")

connection = None

print("Waiting for PostgreSQL to start and accept connections...", flush=True)

# Правильный блок ожидания базы
while True:
    try:
        connection = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        print("Successfully connected to the database!", flush=True)
        break
    except psycopg2.OperationalError as e:
        print(f"Database is not ready yet ({e}), retrying in 3 seconds...", flush=True)
        time.sleep(3)
    except Exception as e:
        print(f"Unexpected error: {e}", flush=True)
        sys.exit(1)

print("Starting main application loop...", flush=True)
try:
    while True:
        time.sleep(10)
finally:
    if connection:
        connection.close()
