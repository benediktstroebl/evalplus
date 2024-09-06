
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
    from string import ascii_lowercase as al
    low = list(al)
    pos = int(len(al) / 2)
    low[pos:] = low[:pos] 
    low[:pos] = low[pos:][::-1]
    res = ''
    for x in s:
        if x in low:
            res += low[low.index(x)]
        else:
            res += x
    return res
