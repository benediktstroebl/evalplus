
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
    shifted_alphabet = [chr(ord(letter) + 2 * i) for i, letter in enumerate(alphabet)]
    encrypted_string = ""
    for letter in s:
        index = s.index(letter)
        encrypted_string += shifted_alphabet[index]
    return encrypted_string
