
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

    rotated_alphabet = []
    rotated_alphabet = alphabet[2:] + alphabet[0:2]
    result = ''
    for letter in s:
        result += rotated_alphabet[alphabet.index(letter)]
    return result

