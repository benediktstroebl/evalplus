
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
    # Initializing the alphabet string
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Converting the string into a list
    s = list(s)
    for i in s:
        # Checking if the characters are in the alphabet list
        if i in alphabet:
            # Shifting the characters by two positions to the right in the list
            s.remove(i)
            s.insert(alphabet.index(i) + 2, i)
        else:
            # Returning the list in string format
            return ''.join(s)
    # Returning the encrypted string
    return ''.join(s)

