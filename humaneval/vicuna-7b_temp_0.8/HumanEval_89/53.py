
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
    # initialize empty string to store the encrypted string
    encrypted = ""
    # loop through each character in the input string
    for char in s:
        # check if the character is a letter
        if char.isalpha():
            # if it is, add it to the encrypted string
            encrypted += char
        else:
            # if it's not a letter, just append it as is
            encrypted += char
    # return the encrypted string
    return encrypted