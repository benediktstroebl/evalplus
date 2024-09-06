
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
    new = ''
    for letter in s:
        # while letter.islower() or letter.isupper():
            # a = ord('a')
            # z = ord('z')
            # A = ord('A')
            # Z = ord('Z')
        if letter.islower():
            a = ord('a')
            z = ord('z')
            new += chr((((ord(letter) - a) * 2) % 26) + a)
        elif letter.isupper():
            A = ord('A')
            Z = ord('Z')
            new += chr((((ord(letter) - A) * 2) % 26) + A)
        else:
            new += letter
    return new
