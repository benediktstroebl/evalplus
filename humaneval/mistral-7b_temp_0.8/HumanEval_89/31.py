
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

    # your code here
    x = 0
    y = 0
    z = ""
    if len(s) > 1:
        for c in s:
            x = ord(c) - 97
            y = (x * 2) % 26
            z += chr(y + 97)
    else:
        z = chr((ord(s) * 2) % 26 + 97)
    return z
