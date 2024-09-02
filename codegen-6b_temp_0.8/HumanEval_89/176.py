
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
    shift = 2
    alphabet = 'abcdefghjklmnpqrstuvwxyz'
    encrypted = ''
    for letter in s:
        pos = alphabet.find(letter)
        new_pos = (pos + shift) %26
        encrypted += alphabet[new_pos]
    return encrypted

