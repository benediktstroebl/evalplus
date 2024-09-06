
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
    a = list(s)
    i = 0
    while i < len(a):
        if a[i].isalpha():
            a.insert(i, a.pop(i+1))
            i += 2
        else:
            i += 1
    return ''.join(a)
    
    

