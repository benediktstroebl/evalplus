
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
    # Your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_two_places = alphabet * 2
    result = ''
    for c in s:
        result += alphabet_two_places[alphabet_two_places.index(c) + 2]

    return result

