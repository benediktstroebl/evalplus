
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
    l = [s[x] for x in range(len(s))]
    l = l[0:5]
    for x in range(5):
        if l[x] == l[4]:
            l[x] = l[x+1]
    r = ''
    for x in range(len(l)):
        r += l[x]
    return r
