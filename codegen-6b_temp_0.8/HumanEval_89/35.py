
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
    # Create a alphabet list
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    # Create a new list of the alphabet rotated 2 places to the left
    rotated = alphabet[3:] + alphabet[:3]

    # Create a dictionary of the alphabet and rotated alphabet
    rotated_dict = dict(zip(alphabet,rotated))

    # Use dictionary lookup to appropriately encrypt the string provided
    new_string = ''.join(rotated_dict.get(letter,letter) for letter in s.lower())
    return new_string
