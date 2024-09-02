
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
    encrypted = ""
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            encrypted += chr((ord(c) - ord('a') + 24) % 26 + ord('a'))
        elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
            encrypted += chr((ord(c) - ord('A') + 24) % 26 + ord('A'))
        else:
            encrypted += c
    return encrypted

