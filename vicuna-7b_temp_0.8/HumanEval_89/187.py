
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
    n = len(s)
    # create a string of zeros
    encrypted = '0' * n
    # rotate the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet[::-1]
    # get the index of the first letter in the string
    i = 0
    for c in s:
        if c.isalpha():
            i += 1
    # rotate the alphabet by the index of the first letter
    alphabet = alphabet[i:] + alphabet[:i]
    # loop through the string
    for c in s:
        if c.isalpha():
            # if the first letter is an uppercase letter, add its rotated equivalent
            # to the encrypted string
            if c.isupper():
                encrypted += alphabet[c.lower()]
            # if the first letter is a lowercase letter, add its rotated equivalent
            # to the encrypted string
            else:
                encrypted += alphabet[c]
        else:
            # if the current character is not an alphabetic character, 
            # add it to the encrypted string as is
            encrypted += c
    return encrypted