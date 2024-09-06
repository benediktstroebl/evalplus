
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

    encrypt_string = ''
    for i in s:
        if i.isalpha():
            letter = ord(i)
            if letter >= 65 and letter <= 90:
                letter = letter + 2 * 2
            if letter >= 97 and letter <= 122:
                letter = letter + 2 * 2
            if letter >= 90 and letter <= 96:
                letter = letter - 2 * 2
            if letter >= 97 and letter <= 122:
                letter = letter - 2 * 2
            encrypt_string = encrypt_string + chr(letter)
        else:
            encrypt_string = encrypt_string + i
    return encrypt_string

