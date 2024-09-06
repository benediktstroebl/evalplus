
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
    s = list(s)
    alpha = [x for x in "abcdefghijklmnopqrstuvwxyz"]
    alpha = alpha[2:] + alpha[:2]
    for i in range(len(s)):
        if s[i] in alpha:
            s[i] = alpha[alpha.index(s[i])]
    s = "".join(s)
    return s


