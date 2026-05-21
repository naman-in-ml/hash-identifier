# This is the first version where i just stored and know the lenght of the hash 
print("This is a simple script to demonstrate a hash identifier.")
hash_value = input("Paste a hash value to identify its type: ") # Get the hash value from the user
print("Length:", len(hash_value)) # length of the hash value

# Now i have to check each char in string with hash characters

valid_characters = "0123456789abcdefABCDEF" # Valid characters for hexadecimal hashes
if all(char in valid_characters for char in hash_value):
    print("The hash value contains only valid hexadecimal characters.")
else:    print("The hash value contains invalid characters for a hexadecimal hash.")

# Version 0.2
# Now we will identify the hash type based on its length
if len(hash_value) == 32:
    print("This is likely an MD5 hash.")
elif len(hash_value) == 40:
    print("This is likely a SHA-1 hash.")
elif len(hash_value) == 64:
    print("This is likely a SHA-256 hash.")
elif len(hash_value) == 128:
    print("This is likely a SHA-512 hash.")
else:
    print("Hash type is unknown or not supported.")

