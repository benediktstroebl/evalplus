
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

    c = list(s)
    l = list(map(chr, range(97, 123)))
    for i in range(len(s)):
        if l[i] in c:
            c[c.index(l[i])] = l[i + 2]
    return ''.join(c)

