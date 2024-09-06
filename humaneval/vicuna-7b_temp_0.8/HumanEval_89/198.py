
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
    # Create a copy of the original string
    s = s.upper()
    # Convert the string to a list of characters
    chars = s.split()
    # Create a new list to hold the encrypted characters
    encrypted = [chr(ord(ch) + 27) for ch in chars]
    # Join the encrypted characters back into a string
    return ''.join(encrypted)
