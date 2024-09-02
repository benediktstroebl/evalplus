
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
    result = ''
    for char in s:
        if char == ' ':
            result += ' '
            continue
        number = ord(char)
        if number >= 65 and number <= 90:
            number = (number + 2 * 2 - 65) % 26 + 65
        elif number >= 97 and number <= 122:
            number = (number + 2 * 2 - 97) % 26 + 97
        result += chr(number)
    return result

