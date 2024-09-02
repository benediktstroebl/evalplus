
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
    lst = []
    for i in s:
        if i == ' ':
            lst.append(i)
        else:
            for c in range(97,123):
                if i == chr(c):
                    lst.append(chr(c+2))
                elif i == chr(c+2):
                    lst.append(chr(c))
    return ''.join(lst)





