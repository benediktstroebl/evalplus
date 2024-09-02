
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
    # your code here
    # return your answer here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet*2
    result = ""
    for char in s:
        if char in alphabet:
            result += alphabet[(alphabet.index(char) + 2*2) % len(alphabet)]
        else:
            result += char
    return result





