
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
    s = list(s)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {}
    for i, letter in enumerate(alpha):
        alpha_dict[letter] = alpha[i:i+2]

    new_str = ''
    for letter in s:
        if letter in alpha_dict:
            new_str += alpha_dict[letter][1]
            new_str += alpha_dict[letter][0]
        else:
            new_str += letter
    return new_str
