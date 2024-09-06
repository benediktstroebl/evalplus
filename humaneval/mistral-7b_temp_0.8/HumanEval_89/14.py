
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
    list = []
    for x in s:
        list.append(ord(x))
    temp = []
    for x in list:
        if x != 32:
            if 97 <= x <= 122:
                temp.append(chr((x + 2 * 2) % 26 + 97))
            elif 65 <= x <= 90:
                temp.append(chr((x + 2 * 2) % 26 + 65))
        else:
            temp.append(chr(32))
    return ''.join(temp)


