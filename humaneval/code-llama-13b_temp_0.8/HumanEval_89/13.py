
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
    rotated = ''
    for letter in s:
        letter = ord(letter)
        if letter <= 122 and letter >= 97:
            if (letter - 2) < 97:
                new_letter = letter + 24
            else:
                new_letter = letter - 2
            rotated += chr(new_letter)
        else:
            rotated += chr(letter)
    return rotated

