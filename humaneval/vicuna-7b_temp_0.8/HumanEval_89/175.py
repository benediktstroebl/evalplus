
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
    rot_alphabet = dict(zip(letters, list(letters)[::-1]))
    rot_letters = set(rot_alphabet.keys())
    encrypted_string = ''
    for letter in s:
        if letter in rot_letters:
            encrypted_string += rot_letters.remove(letter)
        else:
            encrypted_string += letter
    return encrypted_string
