
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
    encrypted_list = []
    for letter in s:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            encrypted_list.append(chr(ord('a') + ((ord(letter) - ord('a') + 2) % 26)))
        else:
            encrypted_list.append(letter)
    return ''.join(encrypted_list)
