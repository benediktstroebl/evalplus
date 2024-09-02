
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
    # your code goes here
    enc_list = []
    l = len(s)
    for i in range(l):
        if s[i].isalpha():
            enc_list.append(chr((ord(s[i]) + 22 - 97) % 26 + 97))
        else:
            enc_list.append(s[i])
    return "".join(enc_list)



