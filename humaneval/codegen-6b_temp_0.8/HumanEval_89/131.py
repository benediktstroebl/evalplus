
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
    def rot(s):
        x = 'abcdefghijklmnopqrstuvwxyz'
        y = 'cdefghijklmnopqrstuvwxyzab'
        z = 'bdefghijklmnopqrstuvwxyza'
        n = s.lower()
        rotated = x[x.index(n)-2:x.index(n)] + y[y.index(n)-2:y.index(n)] + z[z.index(n)-2:z.index(n)]
        return rotated

    return rot(s)

    
