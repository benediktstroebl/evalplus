
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
    n = 2
    
    c = []
    for i in range(0, len(s)):
        c.append(s[i])
    for i in range(0, len(s)):
        a = c[(i+n)%len(c)]
        b = c[(i+n+1)%len(c)]
        c.append(a)
        c.append(b)
    return ''.join(c
