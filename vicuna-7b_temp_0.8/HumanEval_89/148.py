
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
    # Create an empty list to hold the encrypted characters
    encrypted = []
    # Loop through the string
    for i in range(len(s)):
        # If the current character is not a letter, it should be ignored
        if not s[i].isalpha():
            continue
        # Find the index of the character in the alphabet
        index = s[i].upper() - 'A'
        # If the index is greater than 25, the character should be ignored
        if index > 25:
            continue
        # Add the character to the encrypted list
        encrypted.append(chr(index + 25))
    return ''.join(encrypted)
