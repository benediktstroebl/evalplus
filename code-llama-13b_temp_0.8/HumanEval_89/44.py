
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
    a = ''
    for l in s:
        if l.isalpha():
            if l.isupper():
                a += chr((((ord(l) - 65) + 2) % 26) + 65)
            else:
                a += chr((((ord(l) - 97) + 2) % 26) + 97)
        else:
            a += l
    return a

