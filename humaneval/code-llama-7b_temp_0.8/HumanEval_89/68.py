
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
    s = s.lower()
    letters = list(s)
    d = {}.fromkeys(string.ascii_lowercase[:12] + string.ascii_lowercase[-12:])
    k = 0
    for i in d:
        d[i] = string.ascii_lowercase[k]
        k += 2
    return ''.join([d[i] for i in letters])
