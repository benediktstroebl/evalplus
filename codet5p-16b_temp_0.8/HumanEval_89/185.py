
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

    my_list = []
    my_string = 'abcdefghijklmnopqrstuvwxyz'
    my_list = my_string[:26]
    new_string = my_list[2:] + my_list[:2]
    new_list = []
    for letter in s:
        new_list.append(new_string[ord(letter) - ord('a')])
    return ''.join(new_list)


