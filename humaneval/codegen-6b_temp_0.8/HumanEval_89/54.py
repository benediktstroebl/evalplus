
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = {}
    new_s = ''
    for letter in alphabet:
        d[alphabet.index(letter)] = alphabet[alphabet.index(letter)+2]
    for letter in s:
        if letter.isalpha:
            new_s += d[alphabet.index(letter)]
        else:
            new_s += letter
    return new_s
