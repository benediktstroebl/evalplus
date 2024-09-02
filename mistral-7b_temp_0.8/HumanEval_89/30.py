
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
    new_list=[]
    for i in range(len(s)):
        c=ord(s[i])
        if(c<65):
            new_list.append(chr(c+26))
        elif(c>90):
            new_list.append(chr(c-26))
        else:
            new_list.append(chr(c+2))
    return ''.join(new_list)

