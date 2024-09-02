
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
    # create a string
    # for each char in string, find it's position in alphabet
    # set a new variable to the position
    # rotate the position by two, multipled by two
    # find the new character in the alphabet at that position
    # append that to the new string
    # return the new string
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_s = ''
    for char in s:
        index = alphabet.find(char)
        new_index = (index + 2*2) % 26
        new_char = alphabet[new_index]
        new_s += new_char
    return new_s
