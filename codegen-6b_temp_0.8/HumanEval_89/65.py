
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
    alphabet = [chr(i) for i in range(97,123)]
    
    rotated_alphabet = alphabet[1:27]+alphabet[0:1]+alphabet[27:]+alphabet[:1]
    
    return ''.join([rotated_alphabet[alphabet.index(s[i])] for i in range(len(s))])
