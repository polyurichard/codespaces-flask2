import json

# Open and read the JSON file
with open('students.json', 'r') as file:
    data = json.load(file) # Load the JSON data

# Access the list of students
students = data["students"]

# Iterate over each student and print their details
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()  # Print a blank line for better readability