
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
    s = s.lower()
    return_string = ""

    for i in range(0, len(s)):
        current_letter = s[i]
        position_of_letter = alphabet.index(current_letter)
        if position_of_letter >= 24:
            position_of_letter = position_of_letter - 24
        else:
            position_of_letter = position_of_letter + 24
        return_string = return_string + alphabet[position_of_letter]
    return return_string
