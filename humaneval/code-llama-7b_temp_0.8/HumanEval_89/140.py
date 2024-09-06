
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
    #start with the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #replace the letters in the string with the new alphabet
    new_s = ''
    for char in s:
        if char.lower() in alphabet:
            char_index = alphabet.index(char)
            new_char = alphabet[(char_index+4) % len(alphabet)]
            if char.isupper():
                new_s += new_char.upper()
            else:
                new_s += new_char
        else:
            new_s += char
    return new_s
