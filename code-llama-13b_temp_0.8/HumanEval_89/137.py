
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
    alph = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    alph_dict = {}
    alph_list = list(alph)
    for i in range(len(alph_list)):
        alph_dict[alph_list[i]] = alph_list[(i + 4) % len(alph_list)]
    return ''.join([alph_dict[i] for i in s if i.isalpha()])

