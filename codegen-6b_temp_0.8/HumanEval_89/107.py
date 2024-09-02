
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
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2:]+alphabet[0:2]
    
    first_index = alphabet.index(s[0]);
    second_index = alphabet.index(s[1]);
    
    return rotated_alphabet[(first_index*2+second_index)%26] + rotated_alphabet[(first_index*2)%26]
