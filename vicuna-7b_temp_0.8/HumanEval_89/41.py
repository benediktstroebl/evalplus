
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
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            shift = 2*ord(c) - 2
            encryption_letter = chr(ord(c) + shift)
            return encryption_letter
    return ''
