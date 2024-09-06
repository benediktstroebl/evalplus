
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
    res = ''
    for i in s:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            res += chr((ord(i) - ord('a') + 2) % 26 + ord('a'))
        elif (ord(i) >= ord('A') and ord(i) <= ord('Z')):
            res += chr((ord(i) - ord('A') + 2) % 26 + ord('A'))
        else:
            res += i
    return res

