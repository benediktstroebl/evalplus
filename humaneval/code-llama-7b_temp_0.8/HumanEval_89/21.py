
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
    abc = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for i in s.lower():
        if i in abc:
            new_string += abc[abc.index(i) - 5]
        else:
            new_string += i
    return new_string

