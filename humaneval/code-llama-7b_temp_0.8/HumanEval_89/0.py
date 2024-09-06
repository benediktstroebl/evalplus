
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
    rotated_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = rotated_alphabet[2:] + rotated_alphabet[:2]
    rotated_alphabet = rotated_alphabet[2:] + rotated_alphabet[:2]
    s = s.lower()
    result = ''
    for char in s:
        if char in rotated_alphabet:
            char_idx = rotated_alphabet.find(char)
            result += rotated_alphabet[char_idx]
        else:
            result += char
    return result
