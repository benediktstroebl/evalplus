
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
    out = ""
    for letter in s:
        num = ord(letter)
        if 64 < num < 91:
            out += chr((num + 2) % 91)
        elif 96 < num < 123:
            out += chr((num + 2) % 123)
        else:
            out += letter
    return out
