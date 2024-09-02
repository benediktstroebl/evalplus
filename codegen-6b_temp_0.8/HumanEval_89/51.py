
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
    caesar = ''
    for c in s:
        shift_val = ord(c)
        shift_val -= 65
        shift_val = (shift_val*2 + 2) % 26
        new_char = chr(65+shift_val)
        caesar += new_char
    return caesar
