import pytest
from nick import get_employee_details

def test_get_employee_details():
    # Sample data
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 60000

    # Expected result
    expected_output = (
        "Employee Name: Alice Smith, "
        "Employee ID: E202, "
        "Department: HR, "
        "Salary: 60000.00"
    )

    # Assertion
    assert get_employee_details(name, emp_id, department, salary) == expected_output
