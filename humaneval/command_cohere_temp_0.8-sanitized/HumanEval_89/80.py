def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot_factor = 2
    for char in s:
        index = alphabet.find(char)
        next_index = (index + rot_factor) % len(alphabet)
        encrypted.append(alphabet[next_index])
    return "".join(encrypted)