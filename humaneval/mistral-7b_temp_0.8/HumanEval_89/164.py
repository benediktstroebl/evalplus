
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
    encrypted = ''
    for char in s:
        # calculate the position of the char in the alphabet
        position = ord(char) - ord('a')
        # calculate the position of the char in the rotated alphabet
        position += 2 ** 2
        # append the new char to the encrypted string
        encrypted += chr(position + ord('a'))

    return encrypted

