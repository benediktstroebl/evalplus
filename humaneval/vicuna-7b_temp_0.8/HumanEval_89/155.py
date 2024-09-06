
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
    al = "abcdefghijklmnopqrstuvwxyz"
    i = len(al) - 1
    while i > 0:
        al[i], al[i-1] = al[i-1], al[i]
        i -= 1
    return "".join(al[i] for i in range(len(s)))
