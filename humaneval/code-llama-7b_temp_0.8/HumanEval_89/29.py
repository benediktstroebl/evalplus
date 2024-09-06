
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
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i].isalpha():
            s_list[i] = chr(((ord(s_list[i]) - 97 + 2*2) % 26) + 97)
    return ''.join(s_list)
