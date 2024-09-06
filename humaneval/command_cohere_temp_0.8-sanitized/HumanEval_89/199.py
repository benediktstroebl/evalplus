def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        index = alphabet.find(letter)
        delta = (index + 2) // 2 * 2
        encrypted.append(alphabet[index + delta])
    return ''.join(encrypted)