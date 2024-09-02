
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
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    new_alphabet = alphabet[2:]
    new_alphabet.append(alphabet[0])
    new_alphabet.append(alphabet[1])
    encrypted = ''
    for letter in s:
        if letter in alphabet:
            encrypted += new_alphabet[alphabet.index(letter)]
        else:
            encrypted += letter
    return encrypted
