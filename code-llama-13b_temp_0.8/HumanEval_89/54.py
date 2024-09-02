
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
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_alphabet = original_alphabet[2:] + original_alphabet[:2]

    mapping = dict(zip(original_alphabet, new_alphabet))

    return ''.join([mapping[letter] for letter in s.lower()])
