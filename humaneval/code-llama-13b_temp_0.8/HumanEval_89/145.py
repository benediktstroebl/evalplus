
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_s = ""
    for i in s:
        old_i_index = alphabet.find(i)
        new_i_index = old_i_index + 4
        if new_i_index > 25:
            new_i_index = new_i_index - 26
        new_s += alphabet[new_i_index]
    return new_s

