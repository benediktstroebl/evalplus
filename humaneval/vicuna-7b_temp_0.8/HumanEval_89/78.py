
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
    for i in range(len(s)):
        if s[i:i+2] == 'gh':
            s[i:i+2] = 'jh'
            s[i+2:i+4] = 'd'
        elif s[i:i+2] == 'kl':
            s[i:i+2] = 'lk'
            s[i+2:i+4] = 'j'
        elif s[i:i+2] == 'op':
            s[i:i+2] = 'pqr'
            s[i+2:i+4] = 'o'
        elif s[i:i+2] == 'gf':
            s[i:i+2] = 'hj'
            s[i+2:i+4] = 'd'
        elif s[i:i+2] == 'et':
            s[i:i+2] = 'iq'
            s[i+2:i+4] = 'x'

    return s
