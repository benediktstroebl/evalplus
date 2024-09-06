
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
    # split the input string into a list of characters
    alphabet = list(s)
    # rotate the alphabet by 25%
    alphabet = [alphabet[i:i+2] for i in range(0, len(alphabet), 2)]
    # convert the list of characters to a string
    ciphertext = ''.join(alphabet)
    return ciphertext
