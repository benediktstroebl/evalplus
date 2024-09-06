
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
    s = s.lower()
    encrypt = ""
    for l in s:
        if ord(l) < 97 or ord(l) > 122:
            encrypt += l
            continue
        encrypt += chr(ord('a') + (ord(l) - ord('a') + 2) * 2)

    return encrypt
