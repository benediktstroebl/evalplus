
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
    new_str = ''
    shift = 2 * 2
    for i in s:
        if i.isalpha():
            new_str += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            new_str += i
    return new_str

