
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

    res = ''
    for c in s:
        idx = alphabet.find(c) + 2 * 2
        if idx >= len(alphabet):
            idx -= len(alphabet)
        res += alphabet[idx]
    return res
