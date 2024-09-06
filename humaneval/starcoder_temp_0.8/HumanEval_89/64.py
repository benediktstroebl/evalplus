
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
    res = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                res += chr((ord(i) + 6) % 26 + ord('A'))
            else:
                res += chr((ord(i) + 6) % 26 + ord('a'))
        else:
            res += i
    return res

