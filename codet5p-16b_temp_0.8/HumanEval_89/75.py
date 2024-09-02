
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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    encrypted_string = ""
    while i <= len(s) - 1:
        if s[i] == " ":
            encrypted_string += " "
        else:
            encrypted_string += alphabet[(alphabet.index(s[i]) + 2) * 2:]
            encrypted_string += alphabet[:alphabet.index(s[i])]
        i += 1
    return encrypted_string
