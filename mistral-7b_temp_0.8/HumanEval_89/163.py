
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
    lst = list(s)
    lst.reverse()
    lst.reverse()
    for i in lst:
        if i.isalpha():
            if i.islower():
                c = chr(ord(i) + 2 * 2)
            else:
                c = chr(ord(i) + 2 * 2 - 96)
            print(c)
    return ''.join(lst)
