
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
    offset = 2
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if not isinstance(s, str) or len(s) == 0:
        return s
    res = ''
    for c in s:
        if c not in letters:
            res += c
        else:
            idx = letters.find(c)
            new_idx = idx + 2 * offset
            res += letters[new_idx]
    return res

