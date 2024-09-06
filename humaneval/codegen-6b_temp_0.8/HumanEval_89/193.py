
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
    
    # make a dictionary to store the mapping from letter to alphabet index
    alphabets = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

    # create a string out of the input string
    s = ''.join(s)

    # store the encrypted string in this variable
    new_string = ''

    # rotation index
    i = 0

    # for each character in the input string
    for char in s:
        # increment rotation index
        i = i + 1

        # store the index of the original letter in a variable
        orig_index = alphabets[char]

        # if the index is less than 25
        if orig_index < 25:
            # increment the index of the rotated letter by 2
            rotated_index = (orig_index + i * 2) % 26
            # store the letter in the new string
            new_string += chr(rotated_index)
        # else, if the index is greater than 25, decrement the index by 2
        else:
            rotated_index = (orig_index - i * 2 + 26) % 26
            new_string += chr(rotated_index)

    # return the encrypted string
    return new_string

