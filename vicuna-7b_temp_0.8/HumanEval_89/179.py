
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
    # make a copy of the string to modify
    s = s.lower()
    # build the rotated alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_alphabet = alphabet[::2] + alphabet[1::2] + alphabet[0::2]
    # convert each letter to its rotated equivalent
    rot_s = ''
    for char in s:
        if char.isalnum():
            rot_char = rot_alphabet.index(char)
            rot_s += rot_char
        else:
            rot_s += char
    return rot_s
