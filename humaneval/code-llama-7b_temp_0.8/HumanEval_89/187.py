
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
    # L = string.ascii_lowercase
    # uL = string.ascii_uppercase
    # L2 = uL + L
    # return ''.join([L2[(L2.index(i) + 4) % len(L2)] for i in s])

    # Return the encrypted string
    L = string.ascii_lowercase
    uL = string.ascii_uppercase
    L2 = uL + L
    return ''.join([L2[(L2.index(i) + 8) % len(L2)] for i in s])
