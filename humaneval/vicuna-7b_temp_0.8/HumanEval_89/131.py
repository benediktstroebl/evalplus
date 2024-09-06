
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
    a_rotated = {c: i for i, c in enumerate(string.ascii_uppercase)}
    b_rotated = {c: i for i, c in enumerate(string.ascii_lowercase)}
    a_rotated_shifted = {c: i for i, c in enumerate(a_rotated)}
    for k, v in a_rotated_shifted.items():
        a_rotated_shifted[k] = v + (v//2) % 9
    return "".join(sorted(a_rotated_shifted.keys()))
