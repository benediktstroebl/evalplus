
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
    rot = 2*2
    # add assertion
    assert type(s) == str, "Input is not a string"
    # add assertion
    assert len(s) > 0, "Input string is empty"
    # make the alphabet into a list and get the length
    alphabet_list = list(string.ascii_lowercase)
    alphabet_length = len(alphabet_list)
    # loop through the string
    for i in range(len(s)):
        # get the index of the current character in the alphabet
        char_index = alphabet_list.index(s[i])
        # find the new index, making sure it's between 0 and 25
        new_index = (char_index + rot) % alphabet_length
        # replace the character with the new character
        s = s.replace(s[i], alphabet_list[new_index], 1)
    return s
