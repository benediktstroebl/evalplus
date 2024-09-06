
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

    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(len(s)):
        c = s[i]
        new_index = (alpha.index(c) + 2 * 2) % 26
        result = result + alpha[new_index]
    return result
