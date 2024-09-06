
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
    lst = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                lst.append(chr((ord(char) - 65 + 2 * 2 * 2 + 26) % 26 + 65))
            else:
                lst.append(chr((ord(char) - 97 + 2 * 2 * 2 + 26) % 26 + 97))
        else:
            lst.append(char)
    return ''.join(lst)
