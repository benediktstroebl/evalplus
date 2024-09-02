
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
    
    def encrypt(s):
        LETTERS = 'abcdefghijklmnopqrstuvwxyz'
        rotated = LETTERS[len(LETTERS) - 2:] + LETTERS[:len(LETTERS) - 2]
        return ''.join(rotated[LETTERS.find(c)] for c in s)
    return encrypt
    
    