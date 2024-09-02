
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
    
    encryptedString = ''
    
    # Loop through characters of string
    for c in s:

        # Store character index in s in variable i
        i = alphabet.find(c)

        # Call function to rotate by 2 and multiply by 2
        i += 2
        i = i*2

        # Add rotated index to final string
        encryptedString += alphabet[i % 26]
    
    return encryptedString
