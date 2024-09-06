
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
    #letter_shift = (alphabet[(alphabet.index(letter) + 2*alphabet.index(letter)) % 26])
    #alphabet_rotated = alphabet[(alphabet.index(letter) + 2*alphabet.index(letter)) % 26]
    #return letter_shift
    return ''.join(alphabet[(alphabet.index(c) + 2*alphabet.index(c)) % 26] for c in s)
