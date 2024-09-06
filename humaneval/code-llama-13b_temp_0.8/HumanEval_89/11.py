
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
    
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'cdefghijklmnopqrstuvwxyzab'
    dic = {}
    res = ''
    for i in range(len(a)):
        dic[a[i]] = b[i]
    for i in s:
        res += dic[i]
    return res

