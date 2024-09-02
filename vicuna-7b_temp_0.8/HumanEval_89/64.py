
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
    i = 0
    ciphertext = []
    for c in s:
        if c.isalpha():
            index = ord(c) - 97
            if index >= 97 and index <= 102:
                ciphertext.append(chr(index - 97))
            else:
                ciphertext.append(chr(index))
        else:
            ciphertext.append(c)
        i += 1
    return ''.join(ciphertext)
