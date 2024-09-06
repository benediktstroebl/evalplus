
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
    for ch in s:
        ascii_val = ord(ch)
        if ascii_val == 32:
            new_string += " "
        elif ascii_val + 4 < 91:
            new_string += chr(ascii_val + 4)
        else:
            new_string += chr(ascii_val + 4 - 26)
    return new_string
