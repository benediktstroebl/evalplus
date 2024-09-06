
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

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_alpha = alpha[2:] + alpha[:2]
    return ''.join([new_alpha[(alpha.find(l) + 2) % 26] if l in alpha else l for l in s])
