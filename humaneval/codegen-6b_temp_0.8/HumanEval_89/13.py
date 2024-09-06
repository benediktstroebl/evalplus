
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
    encrypt_dict = {}
    for i in range(26):
        encrypt_dict[alphabet[i]] = alphabet[(i+2)%26]
    r = ''
    for c in s:
        if c in encrypt_dict:
            r+=encrypt_dict[c]
        else:
            r+=c
    return r
