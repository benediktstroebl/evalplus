
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
    assert len(s) > 0
    
    # "The letters of the alphabet"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(s):
        output = ''
        for char in s:
            # look up the index of the character
            index = alphabet.find(char)
            # add 2*index to the index
            newIndex = index + 2*index
            # handle the case that newIndex overflows the alphabet
            if newIndex >= 26:
                newIndex = newIndex - 26
            output += alphabet[newIndex]
        return output

    return encrypt(s)
