
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

    # Assuming that the string is in a standard way (only lower case letters)
    string = 'abcdefghijklmnopqrstuvwxyz'

    # Creating a string that contains the alphabet shifted two places
    shift = string[2:] + string[:2]

    # Looping over each letter in the string
    for i in range(len(s)):
        # If the letter is in the string
        if s[i] in string:
            # Replacing the letter in the string with it's respective letter in the shifted string
            s = s[:i] + shift[string.index(s[i])] + s[i+1:]

    return s
