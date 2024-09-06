
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
    n = len(s)
    ret = []
    for i in range(n):
        ch = s[i]
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            ret.append(ch)
        elif ch in '0123456789':
            ret.append(ch + chr(ord(ch) + 6))
        else:
            ret.append(chr(ord(ch) + 12))
    return ''.join(ret)
