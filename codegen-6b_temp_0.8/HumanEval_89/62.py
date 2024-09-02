
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
    if not isinstance(s, str):
        return None
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'.lower()
    rotated = alphabet_lower[alphabet_lower.find(s.lower()[0]) : ] + \
             alphabet[-alphabet.find(s[0].lower()) - 1 : ]
    return rotated
