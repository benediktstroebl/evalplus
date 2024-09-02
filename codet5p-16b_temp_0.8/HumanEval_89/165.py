
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

    result = ""
    for x in s:
        if ord(x) >= 65 and ord(x) <= 90:
            x = chr(ord(x) + 2 * 2)
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(x) + 2 * 2)
        result += x
    return result
