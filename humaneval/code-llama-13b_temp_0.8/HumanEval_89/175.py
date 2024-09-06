
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
    ascii_a = 97
    ascii_z = 122
    ascii_A = 65
    ascii_Z = 90

    new = []
    for letter in s:
        if letter == ' ':
            new.append(' ')
            continue
        if letter.isupper():
            current = ord(letter) - ascii_A
            current = (current + 2 * 26) % 26
            new.append(chr(ascii_A + current))
        else:
            current = ord(letter) - ascii_a
            current = (current + 2 * 26) % 26
            new.append(chr(ascii_a + current))
    return ''.join(new)

