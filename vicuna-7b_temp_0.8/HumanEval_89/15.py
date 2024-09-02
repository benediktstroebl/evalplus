
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
    # Get the length of the input string
    n = len(s)
    # Create an empty string to store the encrypted string
    encrypted = ""
    # Iterate through the characters of the input string
    for i in range(n):
        # Get the ASCII value of the current character
        c = s[i].encode("utf-8")[0]
        # Add the character to the encrypted string
        encrypted += chr(c + 2)
    return encrypted
