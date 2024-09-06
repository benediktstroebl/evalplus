
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

    output = []
    for char in s:
        if char.isalpha():
            if ord(char) + 2 > ord('z'):
                output.append(chr(ord(char) + 2 - 26))
            else:
                output.append(chr(ord(char) + 2))
        else:
            output.append(char)

    return "".join(output)

