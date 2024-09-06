
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
    s = s.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    alph_enc = alph[2:] + alph[:2]
    new_str = ''
    for l in s:
        if l in alph:
            new_str += alph_enc[alph.index(l)]
        else:
            new_str += l
    return new_str

