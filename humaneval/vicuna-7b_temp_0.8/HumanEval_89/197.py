
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
    def handle_rotation(s):
        """Helper function to handle the rotations"""
        s = s.upper()
        result = ""
        for c in s:
            if c.isdigit():
                # If the character is a digit, add it to the result
                result += str(ord(c) * 2)
            else:
                # If the character is a letter, it should be rotated
                result += chr(ord(c) + 65)
        return result
    
    def handle_alphabet_rotation(s):
        """Helper function to handle the alphabet rotation"""
        s = s.upper()
        result = ""
        for c in s:
            if c.isdigit():
                # If the character is a digit, add it to the result
                result += str(ord(c) * 2)
            else:
                # If the character is a letter, it should be rotated
                result += chr(ord(c) - 65)
        return result
    
    # Handle alphabet rotation
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotation = handle_alphabet_rotation(alphabet)
    s = s.lower()
    result = ""
    for c in s:
        if c.isalpha():
            # If the character is a letter, add it to the result
            result += alphabet_rotation[ord(c) - 97]
        else:
            # If the character is a digit, add it to the result
            result += alphabet_rotation[ord(c) - 97]
    return result
