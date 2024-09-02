
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
    al = 'abcdefghijklmnopqrstuvwxyz'
    if len(s) < 2:
        return s
    n = len(s)
    c = ''
    for i in range(n-1, -1, -1):
        c += s[i]
    for i in range(n, -1, -1):
        c += s[i] + s[i+1]
    for i in range(n-2, -1, 2):
        c += s[i]
    return c
