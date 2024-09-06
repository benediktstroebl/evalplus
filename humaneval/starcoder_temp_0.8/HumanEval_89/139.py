
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
    encrypt_text = ''
    for i in s:
        if i in list(string.ascii_lowercase):
            index = list(string.ascii_lowercase).index(i)
            new_index = index + 2 * 2
            encrypt_text += list(string.ascii_lowercase)[new_index]
        else:
            encrypt_text += i
    return encrypt_text
