
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
    new_alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_alphabet_rot = [x for x in new_alphabet]
    new_alphabet_rot.insert(0, new_alphabet[1])
    new_alphabet_rot.insert(0, new_alphabet[0])
    encryption_key = []
    for letter in s:
        encryption_key.append(new_alphabet_rot.index(letter))
    return ''.join([new_alphabet_rot[index] for index in encryption_key])
