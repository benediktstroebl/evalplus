
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
    a= 'abcdefghijklmnopqrstuvwxyz'
    b = ''
    for i in s:
        if i in a:
            b+=a[a.index(i)+2*2]
        elif i in a.upper():
            b+=a.upper()[a.upper().index(i)+2*2]
        else:
            b+=i
    return b
    
