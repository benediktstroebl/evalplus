
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
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(((ord(s[i])-65+2*2*2)+26)%26+65)
        elif s[i].islower():
            s[i] = chr(((ord(s[i])-97+2*2*2)+26)%26+97)
        else:
            s[i] = s[i]
    return ''.join(s)
