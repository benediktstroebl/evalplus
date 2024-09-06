
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num_of_rotation = 2 # This is the number of times the alphabet needs to be rotated
    rotated_alphabet = [chr(i + (j % num_of_rotation) % 26) for i, j in zip(rotation, alphabet)]
    return ''.join(rotated_alphabet[s.index(letter) + j * 2 for letter, j in zip(s, rotation)])
