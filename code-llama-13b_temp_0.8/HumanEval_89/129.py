
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
    
    if not s:
        return ''
    
    res = []
    
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            res.append(chr((ord(char) - ord('a') + 2) % 26 + ord('a')))
        elif ord(char) >= ord('A') and ord(char) <= ord('Z'):
            res.append(chr((ord(char) - ord('A') + 2) % 26 + ord('A')))
        else:
            res.append(char)
    
    return ''.join(res)
