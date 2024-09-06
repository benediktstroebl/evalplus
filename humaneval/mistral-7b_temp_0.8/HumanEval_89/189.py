
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
    list_1 = list(s)
    for i in range(len(list_1)):
        if list_1[i] == ' ':
            list_1[i] = ' '
        else:
            list_1[i] = chr((ord(list_1[i]) - 97) * 2 + 97)
    return ''.join(list_1)

