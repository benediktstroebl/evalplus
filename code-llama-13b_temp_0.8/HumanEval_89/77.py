
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
    if len(s) % 2 == 0:
        start = 2
    else:
        start = 3
    d = dict()
    for i in range(start):
        d[s[i]] = s[i+2]
        d[s[i+2]] = s[i]
    return ''.join(d[i] for i in s if i in d)

