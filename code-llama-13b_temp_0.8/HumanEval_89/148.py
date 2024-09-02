
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
    new_alphabet = ''
    for x in range(2,26,2):
        new_alphabet += alphabet[x:] + alphabet[:x]
    encrypted = ''
    for char in s:
        if char in alphabet:
            encrypted += new_alphabet[alphabet.index(char)]
        else:
            encrypted += char
    return encrypted
