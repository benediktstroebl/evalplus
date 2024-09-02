
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
    s = s.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet[alphabet.index('a'):alphabet.index('z')+1]
    encrypted = []
    for char in s:
        if char.isalpha():
            index = alphabet.index(char)
            index = index - 2 # rotate by 2 places
            encrypted.append(alphabet[index])
        else:
            encrypted.append(char)
    return ''.join(encrypted)
