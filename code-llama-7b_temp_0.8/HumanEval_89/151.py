
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
    encrypted_string = ''
    for letter in s:
        if letter == ' ':
            encrypted_string += ' '
        else:
            encrypted_string += chr(96 + ((ord(letter) - 96) * 4))
    return encrypted_string

