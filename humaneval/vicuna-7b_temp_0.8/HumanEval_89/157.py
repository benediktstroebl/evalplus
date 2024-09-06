
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = len(alphabet) - 1
    encrypted = ''
    while s:
        if i > 0:
            i -= 1
        if i < 0:
            i += len(alphabet)
        if i == 0:
            e = s[0]
            s = s[1:]
            if e == alphabet[e-1]:
                e -= 1
            if e == alphabet[e-1]:
                e -= 1
            if e == alphabet[e-1]:
                e -= 1
            encrypted = encrypted + e
        else:
            if alphabet[i] == s[0]:
                encrypted = encrypted + alphabet[i]
                s = s[1:]
            else:
                s = s[1:]
    return encrypted
