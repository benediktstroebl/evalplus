
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
    rotated_list = []
    # rotated_string = ''
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            if ord(c) - 2 < ord('a'):
                rotated_list.append(chr(ord(c) + 24))
            else:
                rotated_list.append(chr(ord(c) - 2))
        else:
            rotated_list.append(c)

    return ''.join(rotated_list)
    # return rotated_string

