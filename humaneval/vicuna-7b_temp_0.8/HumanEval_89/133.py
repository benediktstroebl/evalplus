
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

    # convert the input string to a list of characters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    words = s.split()
    encrypted_words = []

    for word in words:
        # append each word to the encrypted_words list
        encrypted_words.append(word)

    for i in range(len(words)):
        # rotate the alphabet by 2 places
        alphabet = alphabet[::-1]
        for j in range(len(words[i])):
            # shift each letter of the word down by two places
            encrypted_words[i] = encrypted_words[i][::2]

        # append the encrypted word to the encrypted_words list
        encrypted_words.append(encrypted_words[i])

    return ''.join(encrypted_words)