
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
    encrypted_message = ''
    for letter in s:
        if letter =='':
            encrypted_message +=''
        else:
            index = alphabet.find(letter)
            new_index = index + 2*2
            encrypted_message += alphabet[new_index]
    return encrypted_message
