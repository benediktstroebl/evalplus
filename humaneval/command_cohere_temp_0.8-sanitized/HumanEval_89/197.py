def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifts = [2, 2]

    for char in s:
        index = alphabet.find(char)
        shifted_index = (index + shifts[0] * shifts[1]) % len(alphabet)
        encrypted.append(alphabet[shifted_index])

    return ''.join(encrypted)