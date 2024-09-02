
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
    string_list = list(s)
    new_string = ""
    for char in string_list:
        char_index = alphabet.find(char)
        if char_index!= -1:
            new_string += alphabet[(char_index + 2) % len(alphabet)]
        else:
            new_string += char
    return new_string

