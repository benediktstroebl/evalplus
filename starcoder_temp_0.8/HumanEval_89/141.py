
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
    for char in s:
        if char in ascii_lowercase:
            index = ascii_lowercase.index(char)
            result += ascii_lowercase[(index + 2) % len(ascii_lowercase)]
        elif char in ascii_uppercase:
            index = ascii_uppercase.index(char)
            result += ascii_uppercase[(index + 2) % len(ascii_uppercase)]
        else:
            result += char
    return result
