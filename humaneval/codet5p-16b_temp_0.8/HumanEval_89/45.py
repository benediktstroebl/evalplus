
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

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encrypted_word = ''
    for letter in s:
        if letter.isalpha():
            if letter.islower():
                if alphabet.index(letter) + 2 <= 25:
                    encrypted_word += alphabet[alphabet.index(letter) + 2]
                else:
                    encrypted_word += alphabet[alphabet.index(letter) + 2 - 26]
            if letter.isupper():
                if alphabet.index(letter) + 2 <= 25:
                    encrypted_word += alphabet[alphabet.index(letter) + 2].upper()
                else:
                    encrypted_word += alphabet[alphabet.index(letter) + 2 - 26].upper()
        else:
            encrypted_word += letter
    return encrypted_word
