
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
    encrypt_map = {
        'a': alph[1], 'b': alph[0], 'c': alph[2], 'd': alph[3],
        'e': alph[4], 'f': alph[5], 'g': alph[6], 'h': alph[7],
        'i': alph[8], 'j': alph[9], 'k': alph[10], 'l': alph[11],
        'm': alph[12], 'n': alph[13], 'o': alph[14], 'p': alph[15],
        'q': alph[16], 'r': alph[17], 's': alph[18], 't': alph[19],
        'u': alph[20], 'v': alph[21], 'w': alph[22], 'x': alph[23],
        'y': alph[24], 'z': alph[25]
    }
    new_alph = []
    for ch in s:
        if ch in alph:
            new_alph.append(encrypt_map[ch])
        else:
            new_alph.append(ch)
    return ''.join(new_alph)
