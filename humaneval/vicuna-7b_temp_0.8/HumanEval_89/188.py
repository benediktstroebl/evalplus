
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
    new_alphabet = alphabet[::-1]
    encrypted_string = ''
    for char in s:
        if char.isalpha():
            index = ord(char) - 97
            encrypted_string += new_alphabet[index // 2]
        else:
            encrypted_string += char
    return encrypted_string
