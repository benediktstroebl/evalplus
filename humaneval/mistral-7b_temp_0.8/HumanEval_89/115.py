
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    len = len(s)
    j = 0
    while j < len:
        s[j] = alphabet[alphabet.index(s[j]) + 2*2]
        j += 1
    return s


