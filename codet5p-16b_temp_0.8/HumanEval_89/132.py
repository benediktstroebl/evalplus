
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

    encrypt_dic = {'a': 'e', 'b': 'k', 'c': 'x', 'd': 'w', 'e': 'g', 'f': 'u', 'g': 'j', 'h':'m', 'i': 'c', 'j': 'z', 'k': 'n', 'l': 't','m': 'r', 'n': 'i', 'o': 'b', 'p': 'l', 'q': 'd', 'r': 'y','s': 'a', 't': 'p', 'u': 'h', 'v': 'f', 'w': 'v', 'x':'s', 'y': 'q', 'z': 'o'}
    new_string = ''
    for char in s:
        if char.isalpha() == True:
            new_string += encrypt_dic[char]
        else:
            new_string += char
    return new_string
