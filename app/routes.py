from flask import jsonify, request
from .models import Employee, db
from app import app
from sqlalchemy.exc import IntegrityError


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    serialized_employees = [{
        'id': emp.id,
        'name': emp.name,
        'email': emp.email,
        'phone_number': emp.phone_number,
        'department': emp.department
    } for emp in employees]
    return jsonify(serialized_employees), 200

@app.route('/employees', methods=['POST'])
def create_employee():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        department = data.get('department')

        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        employee = Employee(name=name, email=email, phone_number=phone_number, department=department)
        db.session.add(employee)
        db.session.commit()

        return jsonify({'message': 'Employee created successfully', 'id': employee.id}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Duplicate email. Employee with this email already exists.'}), 400


@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    employee = Employee.query.get(id)
    if employee:
        serialized_employee = {
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'phone_number': employee.phone_number,
            'department': employee.department
        }
        return jsonify(serialized_employee), 200
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404

    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone_number = data.get('phone_number')
    department = data.get('department')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    employee.name = name
    employee.email = email
    employee.phone_number = phone_number
    employee.department = department

    db.session.commit()

    return jsonify({'message': 'Employee updated successfully'}), 200

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404

    db.session.delete(employee)
    db.session.commit()

    return jsonify({'message': 'Employee deleted successfully'}), 200
