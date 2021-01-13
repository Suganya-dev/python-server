EMPLOYEES = [
    {
      "id": 1,
      "name": "Emma Beaton",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Emma Beaton",
      "locationId": 2
    },
    {
      "name": "Sara",
      "locationId": 2,
      "animalId": 6,
      "id": 12
    },
    {
      "name": "divasi",
      "locationId": 2,
      "animalId": 6,
      "id": 13
    }
]

def get_all_employees():
    return EMPLOYEES

        # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee