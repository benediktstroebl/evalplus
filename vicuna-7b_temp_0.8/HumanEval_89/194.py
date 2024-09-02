
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
    # Convert the string to lowercase
    s = s.lower()
    # Create a new string to store the encrypted value
    e = ""
    # Loop through each character in the string
    for c in s:
        # If the character is a printable ASCII character (0x20 or less),
        # add it to the encrypted string with a shifted value
        if c.isdigit() or c.isalpha():
            # Rotate the value of c by two places
            shift = 2 * (ord(c) - ord('0'))
            # Add the rotated value to the encrypted string
            e += chr(shift) + c
        else:
            # If the character is not a printable ASCII character,
            # add it to the encrypted string as is
            e += c
    return e