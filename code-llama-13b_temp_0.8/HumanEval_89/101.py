
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
    for letter in s:
        if letter.islower():
            num = ord(letter) - 96
            num = num - 2*2
            if num < 1:
                num = num + 26
            letter = chr(num + 96)
            encrypted = encrypted + letter
        else:
            num = ord(letter) - 64
            num = num - 2*2
            if num < 1:
                num = num + 26
            letter = chr(num + 64)
            encrypted = encrypted + letter
    return encrypted
