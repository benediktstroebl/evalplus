
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
    n = len(s)
    d = {}
    for i in range(n):
        d[s[i]] = i
    for i in range(n-1, -1, -1):
        d[s[i]] = d[s[i-1]] + 2*d[s[i]]
    return "".join([d[c] for c in s])
