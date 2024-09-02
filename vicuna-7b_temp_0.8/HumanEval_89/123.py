
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
    alphabet = ['abcdefghijklmnopqrstuvwxyz']
    shifted_alphabet = [a + 2*i for i in range(len(alphabet))]
    encrypted = ''
    for char in s:
        if char.isalpha():
            index = alphabet.index(char)
            encrypted += shifted_alphabet[index]
        else:
            encrypted += char
    return encrypted
