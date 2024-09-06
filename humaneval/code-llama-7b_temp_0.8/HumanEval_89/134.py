
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
    letter_dict = {}
    encrypted_s = ''
    for i, letter in enumerate(alphabet):
        letter_dict[letter] = i

    for i, letter in enumerate(s):
        if letter in letter_dict:
            idx = (letter_dict[letter] * 2) % 26
            encrypted_s += alphabet[idx]
        else:
            encrypted_s += letter
    return encrypted_s
