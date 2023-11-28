# 3-Tier web application
- This project outlines the process of building a 3-tier web application using various technologies such as REST API, Python Flask, Docker, PostgreSQL, and Nginx. The application is divided into three tiers: Application, Database, and Frontend.

- Technologies Used
    - REST API
    - Python Flask
    - Docker
    - Python
    - PostgreSQL
    - Nginx (Reverse Proxy)


- Application Tier
The Application Tier is responsible for receiving three parameters (Username, Email, Password), calling the endpoint, and publishing the output to a PostgreSQL database.

- Flask Application:
Flask application using the Flask framework. The application receives parameters (Username, Email, Password) and make API calls.
- Database Interaction:
Store the result of every API call in a PostgreSQL database. 
- Additional API (/view):
    - Create a "/view" API that displays all the contents of the database table.
Database Tier
The Database Tier stores the results of API calls in a PostgreSQL database.

- PostgreSQL Database:  
  - Set up a PostgreSQL database to store the results from the Flask application.
- Dockerization
Docker image of the Flask application for easy deployment.
