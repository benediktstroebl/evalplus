
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
    al = list(s)
    al[0], al[1], al[2], al[3], al[4], al[5], al[6], al[7], al[8] = \
        al[2], al[3], al[4], al[5], al[6], al[7], al[8], al[0], al[1]
    return "".join(al)
