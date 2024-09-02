
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
    new_string = ""
    for i in s:
        if ord(i) in range(65,91):
            if ord(i) > 90 - 2*2:
                new_string += chr(ord(i) - (90 - 2*2))
            else:
                new_string += chr(ord(i) + 2*2)
        elif ord(i) in range(97,123):
            if ord(i) > 122 - 2*2:
                new_string += chr(ord(i) - (122 - 2*2))
            else:
                new_string += chr(ord(i) + 2*2)
        else:
            new_string += i
    return new_string

