
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
    new_alphabet = list(alphabet)
    new_alphabet[0], new_alphabet[1], new_alphabet[2] = new_alphabet[2], new_alphabet[1], new_alphabet[0]
    decoded_string = ""
    for letter in s:
        decoded_string += alphabet[ord(letter) - 64]
    return "".join(decoded_string.split())
