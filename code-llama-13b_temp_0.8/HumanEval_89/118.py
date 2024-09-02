
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
    
    # Solution
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    s_new = ''
    for c in s:
        if c in alpha:
            s_new += alpha[int(alpha.index(c)+2*(alpha.index(c)/26))]
        else:
            s_new += c
    return s_new
