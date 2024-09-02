
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
    shifted_alphabet = [alphabet[i+2*j] for j in range(len(alphabet))]
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            encrypted_char = shifted_alphabet[ord(char) - ord('a')]
            encrypted_string += str(encrypted_char)
        else:
            encrypted_string += char
    return encrypted_string
