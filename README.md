# Employee Management API with Python-Flask

This API allows you to manage employees in a database.

## Installation

1. Clone the repository:

git clone https://github.com/ezekielkibiego/employee-management-api.git

2. Navigate to the project directory:

    ```
    cd employee-management-api
    ```

3. Create a virtual environment:

For Windows

```
python -m venv venv
```

For macOS/Linux

```
python3 -m venv venv
```


4. Activate the virtual environment:

For Windows

```
venv\Scripts\activate
```

For macOS/Linux

```
source venv/bin/activate
```



5. Install dependencies:

```
cd employee-management-api
pip install -r requirements.txt

```


6. Create a `.env` file in the root directory with your database credentials:

```

DB_USER=YOUR_DATABASE_USERNAME
DB_PASSWORD=OUR_DATABASE_PASSWORD
DB_HOST=localhost
DB_PORT=5432
DB_NAME=OUR_DATABASE_NAME
```

7. Run the Flask application:

python run.py


The API will be accessible at http://localhost:5000.

## Endpoints

### GET /employees

Retrieve a list of all employees.

### POST /employees

Create a new employee.

#### Request Body
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone_number": "123-456-7890",
  "department": "HR"
}
GET /employees/{id}
Retrieve an employee by ID.

PUT /employees/{id}
Update an existing employee by ID.

Request Body

{
  "name": "Updated Name",
  "email": "updated.email@example.com",
  "phone_number": "987-654-3210",
  "department": "IT"
}
DELETE /employees/{id}
Delete an employee by ID.
```

This markdown content provides installation instructions, details about available endpoints, and request body examples for creating and updating employees. Adjust the content as needed for your specific API.