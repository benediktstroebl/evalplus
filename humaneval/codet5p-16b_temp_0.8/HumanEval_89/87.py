
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

    my_string = []
    for i in range(len(s)):
        if s[i] == 'z':
            my_string.append('a')
        else:
            my_string.append(chr(ord(s[i]) + 2))
    return ''.join(my_string)
