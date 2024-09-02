
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
    # Create a list of strings representing the alphabet in order
    alphabet = list(string.ascii_uppercase)
    # Rotate the alphabet by shifting letters down by two places
    alphabet = [chr(ord('a') + (i//2*2)) for i in range(len(alphabet))]
    # Use the 'translate' function to replace the original alphabet with the rotated alphabet
    encrypted = ''.join(alphabet.translate(lambda x:x.upper() if x.isupper() else x for x in s))
    return encrypted
