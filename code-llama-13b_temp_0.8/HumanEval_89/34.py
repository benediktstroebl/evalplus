
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
    a = ord('a')
    z = ord('z')
    s1 = []
    for i in s:
        c = ord(i)
        if a <= c <= z:
            s1.append(chr(((c - a) * 2 + a) % 26))
        else:
            s1.append(i)
    return ''.join(s1)
