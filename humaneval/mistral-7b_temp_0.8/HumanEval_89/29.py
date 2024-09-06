
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
    out=""
    for c in s:
        if ord(c) in range(97,123):
            out += chr(ord(c) - 2*2*2)
        elif ord(c) in range(65,91):
            out += chr(ord(c) - 2*2*2)
    return out
    pass
