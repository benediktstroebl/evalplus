
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
    # Your code here
    # This is the normal alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # This is the alphabet shifted down 2 places multiplied to 2 places
    rotate_alphabet = 'cdefghijklmnopqrstuvwxyzab'
    new_str = ''
    # Loop through the string being encrypted
    for letter in s:
        # If the letter is in the normal alphabet
        if letter in alphabet:
            index = alphabet.find(letter)
            new_index = index + 2
            # If the new index is more than 25, subtract 26
            if new_index > 25:
                new_index = new_index - 26
            new_letter = rotate_alphabet[new_index]
            new_str = new_str + new_letter
        # If the letter is not in the normal alphabet
        else:
            new_str = new_str + letter
    return new_str

