
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
    rotated = ""
    # make alphabet a list
    alphabet = list(s)
    # loop through all letters in the list
    for letter in alphabet:
        # convert the letter to an int
        x = ord(letter)
        # add 2 multiplied to 2 places
        x += 2 * 2
        # convert the number back to a letter
        rotated += chr(x)
    return rotated
