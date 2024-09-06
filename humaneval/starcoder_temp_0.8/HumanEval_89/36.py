
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    
    # Store the new string
    encrypted_string = ""

    # Loop through the string, and encrypt every other letter by multiplying it by 2 
    for i in range(0, len(s)):
        if i % 2 == 0:
            encrypted_string += s[i]
        else:
            encrypted_string += chr(ord(s[i]) * 2)

    return encrypted_string

