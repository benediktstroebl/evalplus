
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

    letters = set(s)
    rotated_letters = letters - set(string.ascii_uppercase)
    for letter in rotated_letters:
        rotated_letters.remove(letter)
    rotated_letters = sorted(rotated_letters)
    encrypted = ''
    for letter in rotated_letters:
        encrypted += letter
    return encrypted
