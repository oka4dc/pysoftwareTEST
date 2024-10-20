import re
import json

data = {
    "comment": "Do NOT commit local changes to this file to source control",
    "Internet_hubs": [
        {"id": "men1", "serial_number": "C25CTW00000000001470"},
        {"id": "mn1", "serial_number": "<serial number here>"},
        {"id": "mn2", "serial_number": "<serial number here>"},
        {"id": "mn3", "serial_number": "<serial number here>"},
        {"id": "mn4", "serial_number": "<serial number here>"},
        {"id": "mn5", "serial_number": "<serial number here>"},
        {"id": "mn6", "serial_number": "<serial number here>"},
        {"id": "mn7", "serial_number": "<serial number here>"},
        {"id": "mn8", "serial_number": "<serial number here>"},
        {"id": "mn9", "serial_number": "<serial number here>"}
    ]
}
"""
steps:
1. check if the json data is valid
2. create a list of the serial numbers using kist comprehension
"""
# Function to validate and update the JSON schema
def validate_json_data_and_assign_serial_numbers(data):
    #Validate the structure of the given JSON object
    if "Internet_hubs" not in data:
        raise ValueError("Invalid schema: 'Internet_hubs' key is missing.")
    
    # Declare the serial number range
    serial_start = "C25CTW00000000001470"
    serial_end = "C25CTW00000000001478"
    
    # Generate the list of valid serial numbers with the range function
    serial_range = [f"C25CTW0000000000147{i}" for i in range(8, -1, -1)]
    print(serial_range)
    #Assign serial numbers based on the last digit of "id"
     # declare a new json data to hold the validated data   
    cleaned_data = {"Internet_hubs": []}
    #delare a variable to hold already assigned serial number to avoid repititions
    used_serial_numbers = set()
    
    for hub in data["Internet_hubs"]:
        hub_id = hub["id"]
        print(hub_id)
        
        # Ensure the id is a string and ends with a digit
        if not isinstance(hub_id, str) and not re.match(r'.*\d$', hub_id) and isinstance(hub_id[2], int):
            raise ValueError(f"Invalid id format: '{hub_id}'")
       
        else:
            print("pass")
        """
        # Update the hub with the new serial number
        cleaned_hub = {
            "id": hub_id,
            "serial_number": serial_number
        }
        

"""


validate_json_data_and_assign_serial_numbers(data)