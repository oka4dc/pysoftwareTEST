Given in fig1 is a hypothetical JSON schema, the “Internet_hubs” representing a list of internet hub 
with “id” and “serial number”, A valid serial number has been assigned to the first object with id 
“men1”. The allowed range of serial number is from C25CTW00000000001470 to
C25CTW00000000001478.
Fig1.
{
 "comment": "Do NOT commit local changes to this file to source control",
 "Internet_hubs": [
 {
 "id": "men1",
 "serial_number": "C25CTW00000000001470"
 },
 {
 "id": "mn1",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn2",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn3",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn4",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn5",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn6",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn7",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn8",
 "serial_number": "<serial number here>"
 },
 {
 "id": "mn9", 
 "serial_number": "<serial number here>"

 Task:
As a developer you are tasked with providing a python functionality that can help do the 
following:
•
Validate a given json file/object, or python dictionary to the above schema.
•
If the schema is correct , then assigns the “internet_hubs” a serial number from the range 
given above. The last four digits of the serial number (1470 to 1478) should be used as order
of the serial number and should be assigned in reversed order to the last digit of the Id’s. 
Therefore as shown below{
 "id": "mn1",
 "serial_number": "C25CTW00000000001478"
 },
 {
 "id": "mn9",
 "serial_number": "C25CTW00000000001471"
 } 
•
The function should return a new validated, cleaned and updated json object as well as the 
original objects