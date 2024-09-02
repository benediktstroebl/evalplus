
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
    encrypted_alphabet = alphabet[2:] + alphabet[:2]
    for i in s:
        print(i, encrypted_alphabet.index(i))
        print(alphabet.index(i), encrypted_alphabet.index(i))
        print(alphabet[alphabet.index(i) + 2], encrypted_alphabet[encrypted_alphabet.index(i) + 2])
    encrypted_string = ''
    for i in s:
        encrypted_string += encrypted_alphabet[alphabet.index(i) + 2]
    return encrypted_string
    # return s.translate(str.maketrans(alphabet, encrypted_alphabet))


