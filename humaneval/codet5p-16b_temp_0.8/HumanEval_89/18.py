
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

    encrypt = ''
    for char in s:
        if char.islower():
            new_index = ord(char) - 97 - 2
            if new_index < 0:
                new_index += 26
            encrypt += chr(new_index + 97)
        elif char.isupper():
            new_index = ord(char) - 65 - 2
            if new_index < 0:
                new_index += 26
            encrypt += chr(new_index + 65)
    return encrypt
