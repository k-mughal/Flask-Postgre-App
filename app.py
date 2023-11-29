import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify


# Create the customer table if not exists
CREATE_CUSTOMER_TABLE = (
    "CREATE TABLE IF NOT EXISTS customer (id SERIAL PRIMARY KEY, username TEXT, email TEXT, password TEXT);"
)

#INSERT_CUSTOMER = "INSERT INTO customer (username) VALUES (%s), (email) VALUES (%s), (password) VALUES (%s)"
INSERT_CUSTOMER = "INSERT INTO customer (username, email, password) VALUES (%s, %s, %s)"



load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(url)
cursor = conn.cursor()

CREATE_CUSTOMER_TABLE = (
    "CREATE TABLE IF NOT EXISTS customer (id SERIAL PRIMARY KEY, username TEXT, email TEXT, password TEXT)"
)

cursor.execute(CREATE_CUSTOMER_TABLE)
conn.commit()


# Define the endpoint for creating a new customer
@app.route('/api/customer', methods=['POST'])
def create_customer():
    try:
        # Get data from the request
        data = request.get_json()

        # Extract values from the data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Insert data into the customer table
      
        cursor.execute("INSERT INTO customer (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        conn.commit()

        return jsonify({'message': 'Customer created successfully'}), 201

        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


