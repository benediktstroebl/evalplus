def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        # Multiply char by 2 and rotate alphabet down to find new char position
        index = (alphabet.find(char) + 2) // 2
        encrypted.append(alphabet[index])
    return ''.join(encrypted)