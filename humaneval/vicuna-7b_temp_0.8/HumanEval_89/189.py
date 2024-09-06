
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
    k = []
    j = n - 1
    for i in range(n-1):
        k.append(s[i])
        j -= 1
    for i in range(n-1):
        s[i] = k[j]
        j += 1
    for i in range(n-1):
        k.append(s[i])
        j -= 1
    for i in range(n-1):
        s[i] = k[j]
        j += 1
    return s