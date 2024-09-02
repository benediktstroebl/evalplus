
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
    # create empty string to store the encrypted value
    encrypted = ''
    # loop through each character in the string
    for i, c in enumerate(s):
        # calculate the index of the rotated alphabet
        idx = 97 - (i % 2) * 2
        # append the rotated character to the encrypted string
        encrypted += chr(idx)
    return encrypted
