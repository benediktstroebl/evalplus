
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

    letters = "abcdefghijklmnopqrstuvwxyz"
    new_letters = letters[2:] + letters[:2]
    translated_message = ""
    for i in s:
        translated_message += new_letters[letters.find(i)]
    return translated_message

