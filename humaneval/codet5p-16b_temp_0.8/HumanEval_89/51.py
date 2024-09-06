
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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for i in s:
        if i.lower() in alphabet:
            index = alphabet.find(i.lower()) + 2
            if index > 25:
                index = index - 26
            encrypted += alphabet[index]
        else:
            encrypted += i
    return encrypted
