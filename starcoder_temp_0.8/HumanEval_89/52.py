
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
    s = s.lower()
    j = 0
    out = ""
    for i in s:
        if i.isalpha():
            out = out + chr((((ord(i)-97)+2*j)%26)+97)
            j += 1
        else:
            out = out + i
    return out
