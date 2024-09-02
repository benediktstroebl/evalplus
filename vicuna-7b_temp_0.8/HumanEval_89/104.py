
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
    def _encrypt(s):
        """Helper function that rotates the alphabet and encrypts the input string"""
        rotated_alphabet = 'asdfghjkl'[::-1]
        encrypted_str = ''
        for char in s:
            if char.upper() in rotated_alphabet:
                encrypted_str += rotated_alphabet.index(char.upper())
            else:
                encrypted_str += char
        return encrypted_str
    return _encrypt(s)
