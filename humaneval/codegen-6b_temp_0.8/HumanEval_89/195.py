
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
    
    
    alph = 'abcdefghijklmnopqrstuvwxyz'
    
    def encrypt(x):
        rv = ''
        for i in x:
            rv = i + alph[not alph.index(i)]
        return rv
    return encrypt