
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
    alphabet = ('abcdefghijklmnopqrstuvwxyz'
                'abcdefghijklmnopqrstuvwxyz'
                'abcdefghijklmnopqrstuvwxyz'
                'abcdefghijklmnopqrstuvwxyz'
                'abcdefghijklmnopqrstuvwxyz')
    new_alphabet = []
    for letter in alphabet:
        new_alphabet += letter
        new_alphabet += letter
    for letter in alphabet:
        letter_index = new_alphabet.index(letter)
        new_alphabet[letter_index] = letter
        new_alphabet[letter_index+2] = letter
    new_alphabet = new_alphabet[4:] + new_alphabet[:4]
    return ''.join(new_alphabet[int(new_alphabet.index(letter))]
                   for letter in s)
