
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

    char_list = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
    ]
    enc_list = [
        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m',
        'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y',
        'z', 'a'
    ]
    for index in range(len(char_list)):
        char_list[index] = char_list[index].lower()
    for index in range(len(enc_list)):
        enc_list[index] = enc_list[index].lower()
    enc_list = enc_
