
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
    new_s = ""
    for letter in s:
        if letter == " ":
            new_s += " "
        else:
            new_letter = alphabet[(alphabet.index(letter) + 4) % 26]
            new_s += new_letter
    return new_s
