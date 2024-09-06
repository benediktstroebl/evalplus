def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        if index == -1:
            encrypted += char
        else:
            # Rotate the alphabet by 2 multiplied to 2 places
            # E.g., 'a' becomes 'c' which becomes 'e' etc.
            encrypted += alphabet[(index + 2 * 2) % 26]
    return encrypted