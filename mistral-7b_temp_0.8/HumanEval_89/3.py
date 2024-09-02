
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
    letters_list = list(s)
    letters_list.sort()
    min_letter = letters_list[0]
    max_letter = letters_list[-1]
    shifted_min_letter = chr(ord(min_letter) + 2 * 2)
    shifted_max_letter = chr(ord(max_letter) + 2 * 2)
    new_string = ''
    for letter in letters_list:
        if letter != max_letter:
            new_string += chr(ord(letter) + 2 * 2)
        elif letter != min_letter:
            new_string += shifted_max_letter
        else:
            new_string += shifted_min_letter
    return new_string
