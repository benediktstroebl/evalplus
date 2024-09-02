
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
    alphabet = import_alphabet()
    
    def encrypt_helper(s):
        s = s.lower()
        letter_index = 0
        for letter in s:
            # What do we do when we get to an index past the end of the list?
            character = alphabet[letter_index]
            letter_index += 2
            encrypted_letter = alphabet[letter_index]
            letter_index += 2
            s = s.replace(letter, encrypted_letter)
        return s

    return encrypt_helper

