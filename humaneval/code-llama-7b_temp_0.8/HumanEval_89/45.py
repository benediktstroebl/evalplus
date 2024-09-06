
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
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_rotated = alphabet[-2:] + alphabet[:-2]

    def rot(x):
        return alphabet_rotated[alphabet.index(x)]

    return "".join(rot(l) for l in s)

