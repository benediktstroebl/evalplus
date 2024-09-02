
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
    # return 
    # eg, new_alphabet = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z']
    # eg, original_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_alphabet = 'kjlmnopqrsvwxz'
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    new_alphabet = new_alphabet[(new_alphabet.index(s[0]) + 2) % 26] + new_alphabet[(new_alphabet.index(s[0]) + 2) % 26]
    new_alphabet = new_alphabet[(new_alphabet.index(s[1]) + 2) % 26] + new_alphabet[(new_alphabet.index(s[1]) + 2) % 26]
    new_alphabet = new_alphabet[(new_alphabet.index(s[2]) + 2) % 26] + new_alphabet[(new_alphabet.index(s[2]) + 2) % 26]
    new_alphabet = new_alphabet[(new_alphabet.index(s[3]) + 2) % 26] + new_alphabet[(new_alphabet.index(s[3]) + 2) % 26]

    return new_alphabet
