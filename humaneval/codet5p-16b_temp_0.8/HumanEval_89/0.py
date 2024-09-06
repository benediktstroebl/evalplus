
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
    encrypted_text = ''
    for letter in s:
        index = alphabet.find(letter)
        if index >= 0:
            encrypted_text += alphabet[index + 2*2]
        else:
            encrypted_text += letter
            
    return encrypted_text
    
