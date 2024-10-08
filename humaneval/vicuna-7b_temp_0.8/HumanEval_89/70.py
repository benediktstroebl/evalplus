
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
    if len(s) == 0:
        return s
    x = []
    for c in s:
        if c in string.ascii_uppercase:
            x.append(chr(ord(c) - 26))
        elif c in string.ascii_lowercase:
            x.append(chr(ord(c) + 26))
        else:
            x.append(chr(ord(c) + 48))
    return ''.join(x)
