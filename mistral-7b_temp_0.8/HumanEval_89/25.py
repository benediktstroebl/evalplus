
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
    # Create an empty string to store the encrypted string
    encrypted = ''

    # Loop through each character of the input string
    for char in s:

        # Get the position of the character in the alphabet
        alphabet_pos = ord(char) - 97

        # Rotate the position by the specified amount
        new_pos = (alphabet_pos + 2) % 26

        # Get the encrypted character from the new position
        encrypted += chr(new_pos + 97)

    # Return the encrypted string
    return encrypted
