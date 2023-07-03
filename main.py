import json

# Sample JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON data
data = json.loads(json_data)

# Access JSON values
name = data['name']
age = data['age']
city = data['city']

# Display values
print("Name:", name)
print("Age:", age)
print("City:", city)

# Convert Python object to JSON
json_data = json.dumps(data)
print("JSON Data:", json_data)
