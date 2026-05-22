# This is the first version where i just stored and know the lenght of the hash 

print("This is a simple script to demonstrate a hash identifier.")
hash_value = input("Paste a hash value to identify its type: ") # Get the hash value from the user
print("Length:", len(hash_value)) # length of the hash value
hash_length =  len(hash_value)  # Store the length of the hash value in a variable
valid_characters = "0123456789abcdefABCDEF" # Valid characters for hexadecimal hashes
supported_lengths = [32, 40, 64, 128]
    
# if length is supported then we can identify the hash type, if not then we can say that the hash type is unknown or not supported.
if hash_length in supported_lengths:
    if all(char in valid_characters for char in hash_value):
      print("The hash length is valid for common hash types.")
      if hash_length == 32:   
        print("This is likely an MD5 hash.")
      elif hash_length == 40:
        print("This is likely a SHA-1 hash.")
      elif hash_length == 64:
        print("This is likely a SHA-256 hash.")
      elif hash_length == 128:
        print("This is likely a SHA-512 hash.")
    else:
     print("Hash type is unknown or not supported.")
else:
 print("The hash value contains invalid length.")
 
  

