
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
    # Create an empty string to hold the rotated alphabet
    alphabet = ""
    
    # Loop through the characters in the input string
    for char in s:
        # Add the current character to the rotated alphabet
        alphabet += str(ord(char) + 2)
    
    # Return the encrypted string
    return alphabet
