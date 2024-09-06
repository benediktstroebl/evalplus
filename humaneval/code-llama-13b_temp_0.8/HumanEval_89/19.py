
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
    
    r = s.lower()
    result = []
    for i in r:
        ascii_i = ord(i)
        if 96 < ascii_i < 123:
            if ascii_i > 117:
                new_char_value = ascii_i - 26 + 96
            else:
                new_char_value = ascii_i + 2
            result.append(chr(new_char_value))
        else:
            result.append(i)
    return "".join(result)
