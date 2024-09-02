
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
    # the alphabet length is 26
    alphabet_length = 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # the string to be encrypted
    string_to_encrypt = s

    # empty string to store encrypted message
    encrypted_message = ''

    # iterate through string
    for letter in string_to_encrypt:
        if letter in alphabet:
            # find index of letter in alphabet
            letter_index = alphabet.index(letter)
            # shift the index by two multiplied to two places
            letter_index = letter_index * 2 * 2
            # add shifted index to encrypted message
            encrypted_message += alphabet[letter_index]
        else:
            # if letter is not in alphabet, add it to encrypted message
            encrypted_message += letter

    # return encrypted message
    return encrypted_message

