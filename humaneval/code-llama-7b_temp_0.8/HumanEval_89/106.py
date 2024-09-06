
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
    result = []
    for c in s:
        c = c.lower()
        if ord(c) < ord('a') or ord(c) > ord('z'):
            result.append(c)
        else:
            result.append(chr(ord('a') + (ord(c) - ord('a') + 2) % 26))
    return ''.join(result)

