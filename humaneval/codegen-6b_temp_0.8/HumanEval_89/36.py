
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
    def encrypt_helper(s):
        # Write your encrypt function here.
        rotated_alphabet = rotated_alphabet_generator()
        return ''.join([rotated_alphabet[alphabet.index(letter)] for letter in s])
    return encrypt_helper(s)
