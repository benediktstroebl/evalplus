
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
    # define a dictionary to store the rotated alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotated_alphabet = {}
    for i in range(26):
        rotated_alphabet[alphabet[i]] = i * 2

    # loop through the input string
    result = []
    for char in s:
        # check if the character is in the rotated alphabet
        if char in rotated_alphabet:
            # add the rotated value to the result
            result.append(rotated_alphabet[char])
        else:
            # add the character to the result as is
            result.append(char)

    return ''.join(result)
