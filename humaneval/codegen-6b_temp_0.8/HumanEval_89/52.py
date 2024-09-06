
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
    rotated_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    rotated_alphabet.reverse()
    new_alphabet = []
    for i in range(0, 26, 2):
        new_alphabet.append(rotated_alphabet[i])
        new_alphabet.append(rotated_alphabet[i+1])
    new_alphabet.append(' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' ')
    new_alphabet.insert(0, ' '