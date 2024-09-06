
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

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet2 = list('abcdefghijklmnopqrstuvwxyz'.upper())
    alphabet3 = list('abcdefghijklmnopqrstuvwxyz'.lower())
    
    s = s.lower()
    out = ""
    for x in s:
        out += alphabet3[(alphabet3.index(x) + 2*2)%26]
    return out
