
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
    r = s[::-1]
    a = r.find('a')
    if a == -1:
        return r
    i = r.find('i')
    b = r.find('b')
    if (i == -1 and b == -1) or (b > i):
        return r[:a] + r[b:a+1] + r[a+1:]
    return r[:b] + r[b:b+1] + r[a+1:]


