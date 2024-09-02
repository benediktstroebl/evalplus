
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
    encrypted = ''
    for x in s:
        if x.islower():
            if ord(x) >= 101 and ord(x) <= 122:
                encrypted += chr(ord(x)-24)
            else:
                encrypted += chr(ord(x)+98)
        elif x.isupper():
            if ord(x) >= 70 and ord(x) <= 90:
                encrypted += chr(ord(x)-24)
            else:
                encrypted += chr(ord(x)+64)
        else:
            encrypted += x
    return encrypted
