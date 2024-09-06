
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

    encryption = ''
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                letter = ord(letter)
                encryption += chr(letter + 2 * 2)
            else:
                letter = ord(letter)
                encryption += chr(letter - 2 * 2)
        else:
            encryption += letter
    return encryption

