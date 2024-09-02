
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
    a = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    new = ""
    for l in s:
        if l in a:
            new += a[(a.find(l) + 2 * 2) % 26]
        else:
            new += l
    return new

