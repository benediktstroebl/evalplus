
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
    s_list = []
    for i in s:
        if i.isupper():
            s_list.append(chr((ord(i) - ord('A') + 4) % 26 + ord('A')))
        elif i.islower():
            s_list.append(chr((ord(i) - ord('a') + 4) % 26 + ord('a')))
        else:
            s_list.append(i)

    return ''.join(s_list)
