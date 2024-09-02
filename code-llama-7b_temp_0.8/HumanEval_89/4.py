
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
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    en_alphabet = alphabet[2:] + alphabet[:2]
    result = ""
    for i in s:
        if i in alphabet:
            index = alphabet.index(i)
            result += en_alphabet[index]
        else:
            result += i
    return result
