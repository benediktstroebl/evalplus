
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
    new_str = ""
    for i in range(len(s)):
        if i == len(s) - 1:
            new_str += s[i]
        else:
            if s[i] =='':
                new_str += s[i + 1]
                i += 1
            else:
                new_str += s[i]
    return new_str

