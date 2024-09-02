
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
    result = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for word in s:
        for letter in alpha:
            if word == letter:
                result += alpha[int(alpha.index(letter) + 2) % 26]
    return result
