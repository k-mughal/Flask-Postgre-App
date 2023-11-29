import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, json


# Create the customer table if not exists
CREATE_CUSTOMER_TABLE = (
    "CREATE TABLE IF NOT EXISTS customer (id SERIAL PRIMARY KEY, username TEXT, email TEXT, password TEXT);"
)


load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
conn = psycopg2.connect(url)
cursor = conn.cursor()

CREATE_CUSTOMER_TABLE = (
    "CREATE TABLE IF NOT EXISTS customer (id SERIAL PRIMARY KEY, username TEXT, email TEXT, password TEXT)"
)

# Define the endpoint for creating a new customer
@app.route('/create-customer', methods=['POST'])
def create_customer():
    try:
        # Get data from the request
        data = request.get_json()
    
        # Extract values from the data
        username = data.get('var_username')
        email = data.get('var_email')
        password = data.get('var_password')

        # Insert data into the customer table
        cursor.execute("INSERT INTO customer (username, email, password) VALUES (%s, %s, %s)", (username, email, password))

        conn.commit()

        return jsonify({'message': 'Customer created successfully'}), 201
        
    except Exception as e:
        print(f"Error creating customer: {e}")
        return jsonify({'error': 'Error creating customer'}), 500


# Define the route for rendering the login page
@app.route('/login', methods=['GET'])
def render_login_page():
    return render_template('login.html')



 ######## Define the endpoint for getting information for all customers #########
@app.route('/customers-list', methods=['GET'])
def get_all_customers():
    try:
        # Retrieve all customer information from the database
        cursor.execute("SELECT * FROM customer")
        customers = cursor.fetchall()

        if customers:
            # Convert the result to a list of dictionaries for HTML rendering
            customers_info = []
            for customer in customers:
                customer_info = {
                    'id': customer[0],
                    'username': customer[1],
                    'email': customer[2],
                    'password': customer[3]
                }
                customers_info.append(customer_info)

            # Render an HTML template with the customer information
            return render_template('customer_list.html', customers=customers_info)

        else:
            return render_template('customer_list.html', message='No customers found')

    except Exception as e:
        return render_template('error.html', error=str(e)), 500
    

    