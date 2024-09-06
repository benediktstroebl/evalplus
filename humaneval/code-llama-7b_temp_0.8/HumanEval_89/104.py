
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
    r = 2*2 # rotate by two multiplied to two places
    new = s
    for i in range(len(s)):
        idx = (alpha.index(s[i])+r) % 26
        new = new[:i] + alpha[idx] + new[i+1:]
    return new
