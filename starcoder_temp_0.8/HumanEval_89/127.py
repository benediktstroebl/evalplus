
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
    # Your code here
    key = 2
    rot = key * 2
    encrypt_string = ""
    for character in s:
        if character.isalpha():
            encrypt_string += chr((ord(character) + rot - 97) % 26 + 97)
        else:
            encrypt_string += character
    return encrypt_string
