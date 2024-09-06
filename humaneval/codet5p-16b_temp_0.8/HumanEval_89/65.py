
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
    first_new_letter = alphabet[0]
    second_new_letter = alphabet[1]
    new_alphabet = alphabet[2:]
    new_alphabet = first_new_letter + new_alphabet + second_new_letter
    result = ''
    for letter in s:
        if letter.lower() in alphabet:
            result += new_alphabet[alphabet.index(letter.lower())-2]
        else:
            result += letter
    return result
