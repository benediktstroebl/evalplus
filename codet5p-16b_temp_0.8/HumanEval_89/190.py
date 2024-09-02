
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

    assert s.isalpha()
    char_list = list(s)
    new_char_list = []
    for i in char_list:
        if i.islower():
            new_char_list.append(chr((ord(i) - 97) + 26 - 2 * 2))
        elif i.isupper():
            new_char_list.append(chr((ord(i) - 65) + 26 - 2 * 2))
        else:
            new_char_list.append(i)
    return ''.join(new_char_list)
