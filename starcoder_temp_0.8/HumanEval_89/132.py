
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
    res = ""
    for letter in s:
        pos = ord(letter) - ord('a')
        if letter.isupper():
            if pos < 26 - 2:
                pos += 2
            elif pos == 26 - 2:
                pos = 0
        elif letter.islower():
            if pos < 26 - 2:
                pos += 2
            elif pos == 26 - 2:
                pos = 0
        res += chr(pos + ord('a'))
    return res
