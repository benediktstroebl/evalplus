
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
    s = s.lower()
    encrypted_letters = ''
    for letter in s:
        if letter in alphabet:
            position = alphabet.index(letter) + 2*2
            while position >= 26:
                position -= 26
            encrypted_letters += alphabet[position]
        else:
            encrypted_letters += letter
    return encrypted_letters

