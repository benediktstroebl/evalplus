
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
    # convert string to a list of characters
    letters = list(s)

    # rotate the alphabet by 2 positions
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet[::2] + alphabet[1::2]

    # convert the list of characters to a single string
    encrypted = ''.join(letters)

    # reverse the string
    encrypted = encrypted[::-1]

    # return the encrypted string
    return encrypted
