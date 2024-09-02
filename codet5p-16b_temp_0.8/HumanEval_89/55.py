
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
    new_s = []
    for i in range(len(s_list)):
        if s_list[i].isalpha():
            if s_list[i] in ['a', 'e', 'i', 'o', 'u']:
                new_s.append(s_list[i])
            else:
                new_s.append(chr(ord(s_list[i])-2*2))
        else:
            new_s.append(s_list[i])
    return ''.join(new_s)
