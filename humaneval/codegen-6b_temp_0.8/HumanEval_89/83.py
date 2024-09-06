
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
    encrypted_alphabet = "encrypt this with the alphabet being rotated"
    shifted_alphabet = ""
    for letter in encrypted_alphabet:
        ord_val = ord(letter)
        if ord_val < 65:
            shifted_alphabet += chr(ord_val + 2)
        else:
            shifted_alphabet += chr(ord_val - 2)
    shifted_alphabet = shifted_alphabet[::-1]
    return shifted_alphabet
