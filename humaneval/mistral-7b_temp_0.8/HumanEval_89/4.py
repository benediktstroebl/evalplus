
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

    alphabet_rotated = list(alphabet[2:]) + alphabet[:2]

    # change list to string
    alphabet_rotated = ''.join(alphabet_rotated)

    output = ""
    for letter in s:
        if letter in alphabet:
            # add index of letter in string to index of letter in rotated
            # alphabet
            output += alphabet_rotated[alphabet.index(letter)]
        else:
            output += letter

    return output

