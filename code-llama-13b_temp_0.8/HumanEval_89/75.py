
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
    alph = 'abcdefghijklmnopqrstuvwxyz'
    encrypt = ''
    for ch in s:
        ch = ch.lower()
        if ch in alph:
            encrypt += alph[alph.index(ch) + 4]
        else:
            encrypt += ch
    return encrypt

