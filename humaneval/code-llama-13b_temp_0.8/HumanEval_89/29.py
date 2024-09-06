
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
    ls = list(s)
    for i, c in enumerate(ls):
        char_ord = ord(c)
        # 'a' is 97
        # 'z' is 122
        if 97 <= char_ord <= 122:
            ls[i] = chr((char_ord - 97 + 2 * 26) % 26 + 97)
        # 'A' is 65
        # 'Z' is 90
        if 65 <= char_ord <= 90:
            ls[i] = chr((char_ord - 65 + 2 * 26) % 26 + 65)
    return ''.join(ls)
