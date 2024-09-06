
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
    new_alphabet = alphabet[:]
    for i in range(len(alphabet)):
        if alphabet[i] == 'A':
            new_alphabet[i] = 'J'
        elif alphabet[i] == 'B':
            new_alphabet[i] = 'K'
        elif alphabet[i] == 'C':
            new_alphabet[i] = 'L'
        elif alphabet[i] == 'D':
            new_alphabet[i] = 'M'
        elif alphabet[i] == 'E':
            new_alphabet[i] = 'N'
        elif alphabet[i] == 'F':
            new_alphabet[i] = 'O'
        elif alphabet[i] == 'G':
            new_alphabet[i] = 'P'
        elif alphabet[i] == 'H':
            new_alphabet[i] = 'Q'
        elif alphabet[i] == 'I':
            new_alphabet[i] = 'R'
        elif alphabet[i] == 'J':
            new_alphabet[i] = 'S'
        elif alphabet[i] == 'K':
            new_alphabet[i] = 'T'
        elif alphabet[i] == 'L':
            new_alphabet[i] = 'U'
        elif alphabet[i] == 'M':
            new_alphabet[i] = 'V'
        elif alphabet[i] == 'N':
            new_alphabet[i] = 'W'
        elif alphabet[i] == 'O':
            new_alphabet[i] = 'X'
        elif alphabet[i] == 'P':
            new_alphabet[i] = 'Y'
        elif alphabet[i] == 'Q':
            new_alphabet[i] = 'Z'
        else:
            new_alphabet[i] = alphabet[i]
    return ''.join(new_alphabet)
