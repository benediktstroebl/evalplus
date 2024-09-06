
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
    rotated = alphabet[13:] + alphabet[:13]
    
    def encrypt_r(s):
        s = s.lower()
        encrypted = ''.join([ rotated[alphabet.index(c)] if c in alphabet else c for c in s ])
        return encrypted
    
    return encrypt_r
