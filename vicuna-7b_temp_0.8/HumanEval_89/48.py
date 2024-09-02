
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[::2]
    encrypted_string = ''
    for char in s:
        if char.isalnum():
            encrypted_string += char
        else:
            encrypted_string += rotated_alphabet[ord(char) - 65]
    return encrypted_string
