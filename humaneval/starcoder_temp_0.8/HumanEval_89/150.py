
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
    for char in s:
        # check if letter, else add it as is
        if char.isalpha():
            # check for lowercase
            if char.islower():
                # check if it's a space
                if char == " ":
                    new_string += char
                else:
                    # get the new index and add to string
                    new_string += alphabet[(alphabet.find(char) + 2) % 26]
            # check if it's uppercase
            else:
                # check if it's a space
                if char == " ":
                    new_string += char
                else:
                    # get the new index and add to string
                    new_string += alphabet.upper()[(alphabet.upper().find(char) + 2) % 26]
        # add other characters as they are
        else:
            new_string += char
    return new_string

