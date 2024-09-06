def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        # Find the index of the current letter in the alphabet
        index = alphabet.find(letter)

        # Move the letter two places down in the alphabet and add it to the list
        encrypted.append(alphabet[index - 2:index])
    return ''.join(encrypted)