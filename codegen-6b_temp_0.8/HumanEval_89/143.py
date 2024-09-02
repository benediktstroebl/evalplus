
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
    def encrypt(str):
        old_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_alphabet = 'nopqrstuvwxyzabcdefghij'
        new_str = ''
        for letter in str:
            if letter in old_alphabet:
                new_str += new_alphabet[old_alphabet.index(letter)]
            else:
                new_str += letter
        return new_str
    return encrypt
