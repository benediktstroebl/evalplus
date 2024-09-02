
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_alphabet = []
    for letter in alphabet:
        new_alphabet.append(letter[0])
    while len(new_alphabet) < len(alphabet):
        new_alphabet.append(new_alphabet[-1])
    ciphertext = ""
    for char in s:
        index = s.index(char)
        if index % 2 == 0:
            ciphertext += new_alphabet[index // 2]
        else:
            ciphertext += new_alphabet[(index - 1) // 2]
    return ciphertext
