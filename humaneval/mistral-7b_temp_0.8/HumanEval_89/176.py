
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
    ls = 'abcdefghijklmnopqrstuvwxyz'
    rotate = ls[2:] + ls[:2]
    output = ''
    for c in s:
        output += rotate[ls.find(c)]
    return output
