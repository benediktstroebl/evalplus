
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
    rotate_by = 3
    encrypt_dict = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        encrypt_dict[alphabet[i]] = alphabet[(i + rotate_by) % len(alphabet)]
    return ''.join([encrypt_dict[i] for i in s])
