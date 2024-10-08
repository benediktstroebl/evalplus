python
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
    for c in s:
        if c.isalpha():
            # Shift the character down by 2 multiplied to two places
            shifted = chr(((ord(c) - 97) + 2 * 2) % 26 + 97)
            result += shifted
        else:
            result += c
    return result
