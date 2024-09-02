
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
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = [j for j, k in enumerate(alpha) if k not in "mnbvcxz"]
    
    new_alpha = alpha[num[2]:] + alpha[:num[2]]
    
    table = str.maketrans(alpha, new_alpha)
    
    return s.translate(table)
    