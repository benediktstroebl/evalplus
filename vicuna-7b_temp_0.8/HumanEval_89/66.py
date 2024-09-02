
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
    new_string = ""
    for letter in s:
        if letter.isalpha():
            if letter.lower() in "aeiou":
                new_string += chr((ord(letter) - 97) * 2 + 97)
            elif letter.lower() in "thp":
                new_string += chr((ord(letter) - 97) * 2 + 108)
            else:
                new_string += chr((ord(letter) - 123) * 2 + 123)
        else:
            new_string += letter
    return new_string
