
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
    s_encrypted = ''
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            if ord(i) > 122 - 4:
                s_encrypted += chr(ord(i) - 13)
            else:
                s_encrypted += chr(ord(i) + 4)
        else:
            s_encrypted += i
    return s_encrypted
    
