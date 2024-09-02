
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
    # Create the alphabet with 26 characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # create a variable to hold the new encrypted alphabet
    new_alphabet = alphabet[2:] + alphabet[:2]
    
    # create a function to replace the given character by its corresponding encrypted character
    def replace(c):
        try:
            return new_alphabet[alphabet.index(c)]
        except ValueError:
            return c
    
    # create a variable to hold the encrypted string
    encrypted_string = str()
    
    # loop through the given string to replace the character with its correspoinding encrypted character
    for letter in s:
        encrypted_string += replace(letter)
    
    # return the encrypted string
    return encrypted_string
