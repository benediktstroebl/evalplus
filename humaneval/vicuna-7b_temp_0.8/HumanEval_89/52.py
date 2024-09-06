
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
    encryption_table = {
        'a': 'c', 'b': 'd', 'c': 'a', 'd': 'b', 'e': 'f', 'f': 'e', 'g': 'h', 'h': 'g', 'i': 'j', 'j': 'i',
        'k': 'l', 'l': 'k', 'm': 'n', 'n': 'm', 'o': 'p', 'p': 'o', 'q': 'r', 'r': 'q', 's': 't',
        't': 's', 'u': 'v', 'v': 'u', 'w': 'x', 'x': 'w', 'y': 'z', 'z': 'y'
    }
    encrypted_string = ''
    for char in s:
        encryption_char = encryption_table[char]
        if encryption_char in alphabet:
            encrypted_char = alphabet.index(encryption_char)
        else:
            encrypted_char = encryption_char
        encrypted_string += str(encrypted_char)
    return encrypted_string
