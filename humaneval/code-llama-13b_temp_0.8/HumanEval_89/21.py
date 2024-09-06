
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
    
    def encrypt_char(c):
        # Define a function inside encrypt that takes a character as an argument
        # and returns an encrypted character using the alphabet being rotated.
        # The alphabet should be rotated in a manner such that the letters 
        # shift down by two multiplied to two places.
        # For example:
        # encrypt('a') returns 'm'
        # encrypt('f') returns 'j'
        # encrypt('t') returns 'x'
        letters = [chr(i) for i in range(97, 123)]
        encrypted = letters[2:] + letters[:2]
        return encrypted[ord(c) - 97]

    return ''.join([encrypt_char(c) for c in s if c.isalpha()])
