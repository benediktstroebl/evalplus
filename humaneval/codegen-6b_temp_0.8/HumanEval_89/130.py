
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
    # First create a list of characters to iterate over
    list_of_chars = list(string.ascii_letters)
    # Then sort the list
    list_of_chars.sort()
    # Then use this to build the rotated alphabet
    rotated_alphabet = []
    for i in list_of_chars:
        rotated_alphabet.append(i)
        rotated_alphabet.append(i)
    rotated_alphabet.pop()
    # Now use the itertools to rotate the list
    result = ""
    for letter in s:
        result += rotated_alphabet[ord(letter) - 97]
    return result

