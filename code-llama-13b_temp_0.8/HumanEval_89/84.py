
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
    alpha = "abcdefghijklmnopqrstuvwxyz"
    d = {}
    for i in range(0, 26):
        if i <= 9:
            d[alpha[i]] = alpha[i + 16]
        else:
            d[alpha[i]] = alpha[i + 2]
    
    encrypted_str = ""
    for c in s:
        if c in d:
            encrypted_str += d[c]
        else:
            encrypted_str += c
    return encrypted_str

