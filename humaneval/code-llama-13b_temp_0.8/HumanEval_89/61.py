
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
    res = ""
    for c in s:
        if c.isupper():
            res += chr((ord(c) + 2 - ord('A')) % 26 + ord('A'))
        elif c.islower():
            res += chr((ord(c) + 2 - ord('a')) % 26 + ord('a'))
        else:
            res += c
    return res
