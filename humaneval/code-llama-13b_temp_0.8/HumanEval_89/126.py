
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
    alf = 'abcdefghijklmnopqrstuvwxyz'
    new_alf = ''
    new_alf1 = ''
    for i in range(1,26,2):
        new_alf += alf[i:26]
        new_alf += alf[0:i]
        new_alf1 += alf[i:26]
        new_alf1 += alf[0:i]
    new_alf1 += new_alf[-2:]
    new_alf1 = new_alf1.upper()
    new_alf1 = alf.upper() + new_alf1[26:]
    return s.translate(str.maketrans(alf, new_alf))
