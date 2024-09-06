
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

    # Rotate alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = alphabet[::-1]

    # Generate a key for the encryption
    key = 'aeiouytyuphcndoiaxz'
    key_rotated = key[::-1]

    # Create an empty string for the encrypted message
    encrypted_message = ''

    # Loop through the string to be encrypted and encrypt each character
    for char in s:
        # Determine the index of the character in the rotated alphabet
        rot_index = alphabet_rotated.index(char)

        # Determine the index of the character in the key
        key_index = alphabet_rotated.index(char)

        # Rotate the key to match the rotated alphabet
        key_rotated = key_rotated + 'z' * (26 - len(key_rotated) % 26)

        # Rotate the key and character
        key_rotated, char = char, key_rotated[key_index]

        # Append the encrypted character to the encrypted message
        encrypted_message += chr(ord(char) + rot_index)

    return encrypted_message
