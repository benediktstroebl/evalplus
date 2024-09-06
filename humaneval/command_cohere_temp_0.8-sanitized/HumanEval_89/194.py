def encrypt(string):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate_len = 2
    step = 2

    for char in string:
        index = alphabet.find(char)
        new_index = (index + rotate_len * step) % len(alphabet)
        encrypted += alphabet[new_index]
    return encrypted