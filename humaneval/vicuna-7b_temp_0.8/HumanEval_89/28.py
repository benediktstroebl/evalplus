
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
    alphabets = ['abcdefghijklmnopqrstuvwxyz']
    alphabet_rotated = [alphabets[i:i+2] for i in range(len(alphabets)-1)]
    return ''.join(sorted(list(set(s)), key=lambda x: alphabet_rotated.index(x)))
