
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
    shift = 2
    shift_down = alphabet[shift:] + alphabet[:shift]
    final_alphabet = shift_down[shift:] + shift_down[:shift]
    final_string = ""
    for c in s:
        index = alphabet.index(c)
        final_string += final_alphabet[index]
    return final_string
