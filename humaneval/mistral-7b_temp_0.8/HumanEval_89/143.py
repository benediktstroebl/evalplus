
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
    l = len(s)
    l = l//2
    z = ''
    for i in range(l):
        b = s[i]
        b = ord(b)
        x = b + 12
        x = x % 26
        x = chr(x)
        z = z + x
    for i in range(l, l+1):
        b = s[i]
        b = ord(b)
        x = b + 12
        x = x % 26
        x = chr(x)
        z = z + x
    return z
