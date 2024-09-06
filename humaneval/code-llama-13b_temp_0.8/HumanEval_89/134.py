
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
    l = list(s)
    for i in range(0, len(l)):
        if ord(l[i]) in range(ord('A'), ord('Z')+1):
            l[i] = chr(((ord(l[i])-ord('A')+2)%26)+ord('A'))
        elif ord(l[i]) in range(ord('a'), ord('z')+1):
            l[i] = chr(((ord(l[i])-ord('a')+2)%26)+ord('a'))
    return ''.join(l)
    
    
