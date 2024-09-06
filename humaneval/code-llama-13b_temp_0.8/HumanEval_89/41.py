
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
    new_string = ''
    for letter in s:
        if ord(letter) >= 97 and ord(letter) <= 122:
            if ord(letter) >= 110:
                new_string += chr(ord(letter) + 14)
            else:
                new_string += chr(ord(letter) + 13)
        else:
            new_string += letter
    return new_string

