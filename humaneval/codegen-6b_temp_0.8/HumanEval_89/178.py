
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
    
    n = len(alphabet)
    
    if n == 26:
        return alphabet[n - 2 : ] + alphabet[ : n - 2]
    if n == 26 and n - 2 == 2:
        return alphabet[0 : 4] + alphabet[4 : 8] + alphabet[8:12] + alphabet[12 : 16]
    if n == 26 and n - 2 == 4:
        return alphabet[0 : 4] + alphabet[4 : 8] + alphabet[8:12] + alphabet[12 : 16] + alphabet[16 : ] + alphabet[0 : 4]
    if n - 2 == 26:
        return alphabet[0 : 26] + alphabet[26 :]
    if n - 2 == 26 and n - 2 == 2:
        return alphabet[n - 2 : ] + alphabet[ : n - 2]
    if n - 2 == 26 and n - 2 == 4:
        return alphabet[n - 2 : ] + alphabet[ : n - 2] + alphabet[n - 2 : ] + alphabet[ : n - 2]