
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char_map = {}
    alphabet_ = alphabet[:]
    for i in range(len(alphabet)):
        char_map[alphabet_[i]] = alphabet[i]
        char_map[alphabet[i]] = alphabet_[i]
    sl = list(s)
    for i in range(len(sl)):
        if sl[i] in char_map:
            sl[i] = char_map[sl[i]]
    return ''.join(sl)
