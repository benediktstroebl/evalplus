
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_rotated_n = alphabet[2:] + alphabet[:2]
    char_to_digit = dict((c, i) for i, c in enumerate(alphabet_rotated_n))
    s = [char_to_digit[c] for c in s]
    return ''.join([alphabet_rotated_n[x] for x in s])

