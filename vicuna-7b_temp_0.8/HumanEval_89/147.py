
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
    alp = 'abcdefghijklmnopqrstuvwxyz'
    rot_alp = [alp[i:i+2] for i in range(len(alp) - 1)]
    return ''.join(rot_alp[s.index(i) + 2] for i in s)
