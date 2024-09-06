
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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = 'cdefghijklmnopqrstuvwxyzab'
    result = ''
    for letter in s:
        if letter not in alphabet:
            result += letter
            continue
        rotated_letter = alphabet.index(letter)
        rotated_letter += 2
        rotated_letter %= 26
        result += rotated_alphabet[rotated_letter]
    return result

