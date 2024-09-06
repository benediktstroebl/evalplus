
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
    encrypt_str = ''
    for l in s:
        if l.isalpha():
            if l.isupper():
                encrypt_str += chr((ord(l) + 2) % 26 + ord('A'))
            else:
                encrypt_str += chr((ord(l) + 2) % 26 + ord('a'))
        else:
            encrypt_str += l
    return encrypt_str
