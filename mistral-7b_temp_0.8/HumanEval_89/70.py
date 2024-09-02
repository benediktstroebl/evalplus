
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
    import string
    if s == s.lower():
        s = s.upper()
        return s
    if s == s.upper():
        s = s.lower()
        return s
    s = list(string.ascii_lowercase)
    s = ''.join(s)
    temp = s[26:] + s[:26]
    return ''.join([temp[i + int(2*i)] for i in s])


