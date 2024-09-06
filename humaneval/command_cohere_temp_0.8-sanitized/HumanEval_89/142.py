def encrypt(s):
    """Encrypted a string with a shifted alphabet."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        if index == -1:
            # If the character is not in the alphabet, return it as is.
            encrypted += char
        else:
            # Encrypt the character according to the algorithm.
            encrypted += alphabet[index + 2]*2
    return encrypted