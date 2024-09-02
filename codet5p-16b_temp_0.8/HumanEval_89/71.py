
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

    # create dictionary with all letters in the english alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # create variable to store encrypted letter
    encrypted_letter = ""
    # iterate through each letter of the alphabet
    for letter in alphabet:
        # check if letter is equal to the string
        if letter == s:
            # if so, append letter to encrypted letter
            encrypted_letter += letter
        else:
            # if not equal, append letter to encrypted letter
            encrypted_letter += letter
    return encrypted_letter
