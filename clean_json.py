import json

# Load the JSON data from your file
with open('bookings.json', 'r') as file:
    data = json.load(file)

# Function to recursively remove empty fields
def remove_empty_fields(item):
    if isinstance(item, dict):
        return {k: remove_empty_fields(v) for k, v in item.items() if v not in [None, "", []]}
    elif isinstance(item, list):
        return [remove_empty_fields(i) for i in item if i not in [None, "", []]]
    else:
        return item

# Clean the entire data
cleaned_data = remove_empty_fields(data)

# Save the cleaned data back to the file
with open('bookings_cleaned.json', 'w') as file:
    json.dump(cleaned_data, file, indent=4)

print("Empty fields removed successfully.")
