
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
    # Create a list of the lowercase characters in the string
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabet.lower()
    # Create a new string with the same length as the input string
    encrypted = ''
    for char in letters:
        if char in letters:
            # If the character is in the list of lowercase characters, add
            # its encrypted version to the string
            encrypted += str(ord(char) + 24)
        else:
            # If the character is not in the list of lowercase characters,
            # add a space to the string
            encrypted += ' '
    return encrypted
