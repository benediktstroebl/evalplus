
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
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alpha = alp[1:] + alp[:1]
    reduced_alph = alpha[2:] + alpha[:2]
    # print(s)
    return reduce(lambda x,y: x+y, zip(s,reduced_alph))
