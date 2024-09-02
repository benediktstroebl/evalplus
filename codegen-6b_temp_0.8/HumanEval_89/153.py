
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
    s = ''.join(s.split())
    n = len(s) % 2
    e = alphabet[:len(alphabet) - n]
    f = alphabet[-n:]
    return ''.join( [e[alphabet.index(i)] for i in s] ) + ''.join( [f[alphabet.index(i)] for i in s[::-1]])
