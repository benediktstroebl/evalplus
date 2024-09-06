
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
    res = ""
    for i in s:
        temp = ord(i)
        if i.isupper():
            res += chr((temp + 2*26*2)%26 + 65)
        else:
            res += chr((temp + 2*26*2)%26 + 97)
    return res
