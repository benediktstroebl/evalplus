
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
    # define a list of 26 characters
    alphabet = [chr(i) for i in range(97, 123)]
    new_alphabet = alphabet[1:] + alphabet[0:1]
    # mapper function to shift letters down by two and multiply by two
    mapper = lambda x: new_alphabet[(new_alphabet.index(x)+2)%len(new_alphabet)]*2
    # create an output string
    encrypted = ''
    # map each character in the string
    for character in s:
        encrypted += mapper(character)
    return encrypted
