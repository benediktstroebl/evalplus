
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
    # convert the string to a list of characters and convert each character to its ascii value
    # create a new list that is the original list but with the values incremented by 2**10
    # then convert each character in the list to its ascii value
    # join the characters back into a string
    return ''.join([chr(int(c) + 2**10) for c in s])
