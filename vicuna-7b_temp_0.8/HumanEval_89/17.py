
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
    def key_rotation(char):
        index = char.upper().index("A")
        new_char = chr((ord("A") - index) % 26 + ord("a"))
        return new_char

    def encrypt_string(string):
        result = ""
        for char in string:
            result += key_rotation(char)
        return result
    return encrypt_string(s)
