
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
    t = ""
    for i in s:
        c = i
        if c.isupper():
            c = chr(ord(c)-26*2)
        elif c.islower():
            c = chr(ord(c)-26*2+32)
        t += c
    return t
