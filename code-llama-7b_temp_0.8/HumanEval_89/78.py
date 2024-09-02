
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
    r = ''
    for i in s:
        a = al.find(i)
        a = a + 2*2
        if a >= len(al):
            a = a - len(al)
        r = r + al[a]
    return r
