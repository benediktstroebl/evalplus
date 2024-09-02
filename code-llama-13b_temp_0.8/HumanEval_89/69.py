
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
    res = ''
    for char in s:
        if char.isupper():
            res += chr((ord(char) - 65 + 2) % 26 + 65)
        elif char.islower():
            res += chr((ord(char) - 97 + 2) % 26 + 97)
        else:
            res += char
    return res
