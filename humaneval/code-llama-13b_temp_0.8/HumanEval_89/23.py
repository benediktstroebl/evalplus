
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
    # ...
    # Make a new empty string called new_s
    new_s = ''

    # For each character in s
    for char in s:
        # If the character is in range of 'a' and 'z' or 'A' and 'Z'
        if char.isalpha():
            # ...
            # Find the char's position in the alphabet
            # Add two to the char's position
            # Use mod 26 to ensure the char's position is between 0 and 25
            # Convert this new position to a character
            # Add this new character to new_s
            new_s += chr((ord(char.lower()) + 2 - 97) % 26 + 97)
        # If the character is not in the range...
        else:
            # ...
            # Just add the character to new_s
            new_s += char

    # Return new_s
    return new_s
