
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
    new_alpha = alpha[14:] + alpha[:14]
    new_s = ''
    for c in s:
        if c in alpha:
            new_s += new_alpha[alpha.index(c)]
        else:
            new_s += c
    return new_s

