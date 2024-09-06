
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

    alph = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    alph += [chr(x) for x in range(ord('a'), ord('z') + 1)]

    shift = 2*2
    out = ''

    for char in s:
        if char in alph:
            out += alph[(alph.index(char) + shift) % len(alph)]
        else:
            out += char

    return out
