
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
    # Your code here
    str = list(s)
    for i in range(len(str)):
        if ord(str[i]) + 3 > 122:
            str[i] = chr(ord(str[i]) - 26)
        else:
            str[i] = chr(ord(str[i]) + 3)
    return "".join(str)

