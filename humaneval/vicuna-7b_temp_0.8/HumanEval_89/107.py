
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
    # Define a variable to hold the encrypted string
    encrypted = ''
    # Define a variable to hold the current index of the alphabet
    current_index = 0
    # Loop through each character of the input string
    for char in s:
        # If the character is in the alphabet, add it to the encrypted string
        if char in ALPHABET:
            encrypted += ALPHABET[current_index]
        # If the character is not in the alphabet, add a space to the encrypted string
        else:
            encrypted += ' '
        # Increment the current index by one
        current_index += 1
    return encrypted
