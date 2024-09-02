
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

    # Your code here
    letters = []
    for c in s:
        if c.isalpha():
            x = ord(c)
            x = x + 2
            if x > 122:
                x = x - 26
            letters.append(chr(x))
        else:
            letters.append(c)
    return "".join(letters)

