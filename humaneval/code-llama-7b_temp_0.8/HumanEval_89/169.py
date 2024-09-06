
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
    ab = "abcdefghijklmnopqrstuvwxyz"
    s_list = list(s)
    new_s = []
    for l in s_list:
        if l not in ab:
            new_s.append(l)
        else:
            new_s.append(ab[(ab.index(l) + 4) % len(ab)])
    return "".join(new_s)
