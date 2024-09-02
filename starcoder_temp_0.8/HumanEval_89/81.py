
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
    # your code here
    encrypt = ''
    for i in s:
        if i in alphabet:
            new_index = (alphabet.index(i) + 2) % 26
            encrypt += alphabet[new_index]
        else:
            encrypt += i
    return encrypt
