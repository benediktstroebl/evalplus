
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

    new_str = ""
    for c in s:
        if ord(c) > 96 and ord(c) < 123:
            if ord(c) + 2 > 122:
                new_str += chr(ord(c) + 2 - 26)
            else:
                new_str += chr(ord(c) + 2)
        elif ord(c) > 64 and ord(c) < 91:
            if ord(c) + 2 > 90:
                new_str += chr(ord(c) + 2 - 26)
            else:
                new_str += chr(ord(c) + 2)
        else:
            new_str += c
    return new_str
    
