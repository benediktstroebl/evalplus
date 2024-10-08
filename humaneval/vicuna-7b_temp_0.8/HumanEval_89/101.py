
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
    encrypted = []
    for char in s:
        if char.isalpha():
            idx = ord(char) - 97
            encrypted.append(alphabet[idx // 2 % 26 + idx % 2])
        else:
            encrypted.append(char)
    return ''.join(encrypted)
