
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
    first_letter = s[0].upper()
    last_letter = s[0].lower()
    next_letters = s[1:]
    # print(first_letter)
    # print(last_letter)
    # print(next_letters)
    new_first_letter = chr(ord(first_letter) + 2)
    new_last_letter = chr(ord(last_letter) + 2)
    # print(new_first_letter)
    # print(new_last_letter)
    new_first_letter = new_first_letter.lower()
    new_last_letter = new_last_letter.upper()
    # print(new_first_letter)
    # print(new_last_letter)
    new_letters = new_first_letter + next_letters + new_last_letter
    # print(new_letters)
    return new_letters
    # return 

