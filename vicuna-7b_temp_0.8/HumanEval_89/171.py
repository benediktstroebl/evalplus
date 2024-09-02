
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
    # Rotate the alphabet and convert the string to a tuple
    rot_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = rot_alphabet[::-1]
    input_string = tuple(s)
    # Rotate the string by shifting the letters down by 2 positions
    rotate_string = input_string[::2]
    # Convert the rotated string back to a string
    encrypted_string = ''.join(rotate_string)
    return encrypted_string
