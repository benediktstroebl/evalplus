
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
    import string
    
    def shift_alphabet(s):
        return s[2:] + s[:2]
    
    def rotate(s):
        return ''.join(map(shift_alphabet, s))
    
    return rotate(string.ascii_lowercase) + rotate(string.ascii_uppercase)

