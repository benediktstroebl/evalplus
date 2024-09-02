
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
    letters = set(s)
    rotated_letters = {}
    for letter in letters:
        index = ord(letter) - 97
        rotated_letters[letter] = chr(index // 26) + chr((index % 26) // 26 * 2)
    return ''.join(rotated_letters[letter] for letter in s)
