
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
    new_string = []
    for letter in s:
        index = ord(letter)
        if index <= 90:
            new_index = ((index - 65) + 22) % 26
        else:
            new_index = ((index - 97) + 22) % 26
        new_string.append(chr(new_index + 65))
    return ''.join(new_string)

