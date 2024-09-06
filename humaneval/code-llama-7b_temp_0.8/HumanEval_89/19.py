
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
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    # ZYXWVUTSRQPONMLKJIHGFEDCBA
    # ABDEJFCGIKMLNOPQTUVWXHYZS
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = s.upper()
    x = ""
    for c in s:
        if c in abc:
            x += abc[(abc.index(c)+2)%26]
        else:
            x += c
    return x

