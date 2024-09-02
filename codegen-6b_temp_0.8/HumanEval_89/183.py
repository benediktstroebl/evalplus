
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
    # Create the encrypted alphabet
    encrypted_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Create the altered alphabet
    alphabet_for_shift = encrypted_alphabet[0:len(encrypted_alphabet) / 2]
    alphabet_for_shift.reverse()
    # Store the encrypted alphabet
    encrypted_alphabet = encrypted_alphabet + alphabet_for_shift

    # Shift the encrypted alphabet
    def shift_array(array):
        return array[2:] + array[:2]
    # Store the encrypted alphabet
    encrypted_alphabet = shift_array(encrypted_alphabet)

    repeated_alphabet = encrypted_alphabet * 5

    # Check for invalid characters
    for character in s:
        if character not in repeated_alphabet:
            return False

    # Check for valid characters
    for character in s:
        if character in repeated_alphabet:
            # Compute the position of the character
            pos = repeated_alphabet.index(character)
            # Compute the new position
            new_pos = pos + 2
            # Return the encrypted character
            return encrypted_alphabet[new_pos]

