
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

    rotated_alphabet = alphabet[2:] + alphabet[:2]

    def encrypt(string):
        new_string = ''
        for c in string:
            val = rotated_alphabet.index(c)
            new_string += rotated_alphabet[val]
        return new_string
    return encrypt

