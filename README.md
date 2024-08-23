### Simple CRUD User RESTful API with Django and PostgreSQL

This project is a simple RESTful API for managing user data, built using Python with the Django framework. The API supports basic CRUD (Create, Read, Update, Delete) operations for user management and is backed by a PostgreSQL database.

#### Features:
- **Create User:** Add new users to the database.
- **Read User(s):** Retrieve details of a single user or a list of all users.
- **Update User:** Modify existing user information.
- **Delete User:** Remove a user from the database.

#### Technologies:
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **API Documentation:** Django REST Framework (DRF) browsable API

#### Setup Instructions:
1. Clone the repository:
   ```bash
   git clone https://github.com/mnaufalrifqir/django_api_user.git
   ```
2. Navigate to the project directory:
   ```bash
   cd django_api_user
   ```
3. Install the required dependencies:
   ```bash
   pip install django djangorestframework
   pip install psycopg2
   ```
4. Set up the PostgreSQL database and update the `settings.py` file with your database credentials.
5. Run the migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the API:
   You can access the API at the following URL:
   ```bash
   http://127.0.0.1:8000/api/users/
   ```

#### API Endpoints:
- **POST /api/users/create/**: Create a new user.
- **GET /api/users/**: Retrieve a list of all users.
- **GET /api/users/{id}/**: Retrieve a specific user by ID.
- **PUT /api/users/{id}/**: Update user details.
- **DELETE /api/users/{id}/**: Delete a user by ID.