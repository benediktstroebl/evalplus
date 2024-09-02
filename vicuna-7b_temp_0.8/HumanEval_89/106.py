
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
    def rotate(alphabet):
        """Rotate the alphabet by 2 positions."""
        return [alphabet[i:i+2] for i in range(len(alphabet) - 1)]
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_alphabet = rotate(alphabet)
    encrypted_string = ''
    for char in s:
        encrypted_string += encrypted_alphabet[ord(char) - 65]
    return encrypted_string
