
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
    
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotated_alpha = 'jklmnopqrstuvwxyzabcdefghij'

    shifted_lower_alpha = rotated_alpha[:26]
    shifted_upper_alpha = rotated_alpha[26:]
    
    lower_index = upper_alpha.index(s)
    upper_index = lower_alpha.index(s)
    
    return lower_alpha[lower_index+len(shifted_lower_alpha)] + upper_alpha[upper_index+len(shifted_upper_alpha)]
    
