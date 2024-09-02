
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
    
    #alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    
    two_places = 2
    
    alphabet_with_shifted_letters = alphabet[two_places:] + alphabet[:two_places]
    
    encrypted_string = ''.join(alphabet_with_shifted_letters[alphabet.index(letter) + 2] for letter in s)

    return encrypted_string
