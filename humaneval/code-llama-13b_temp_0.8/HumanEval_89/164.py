
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
    result = ''
    for i in s:
        c = ord(i)
        if c >= 65 and c <= 90:
            c = ((c - 65 + 2) % 26) + 65
        elif c >= 97 and c <= 122:
            c = ((c - 97 + 2) % 26) + 97
        result += chr(c)
    return result

