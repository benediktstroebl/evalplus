
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
    # return None
    result = ''
    for char in s:
        if char == ' ':
            result += ' '
        elif char == 'A':
            result += 'C'
        elif char == 'B':
            result += 'D'
        elif char == 'C':
            result += 'E'
        elif char == 'D':
            result += 'F'
        elif char == 'E':
            result += 'G'
        elif char == 'F':
            result += 'H'
        elif char == 'G':
            result += 'I'
        elif char == 'H':
            result += 'J'
        elif char == 'I':
            result += 'K'
        elif char == 'J':
            result += 'L'
        elif char == 'K':
            result += 'M'
        elif char == 'L':
            result += 'N'
        elif char == 'M':
            result += 'O'
        elif char == 'N':
            result += 'P'
        elif char == 'O':
            result += 'Q'
