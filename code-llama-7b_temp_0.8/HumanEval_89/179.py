
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
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = ''
    for char in s:
        if char in LETTERS:
            num = LETTERS.find(char)
            num = num * 2
            if num > len(LETTERS):
                num = num % len(LETTERS)
            encrypted = encrypted + LETTERS[num]
        else:
            encrypted = encrypted + char
    return encrypted

