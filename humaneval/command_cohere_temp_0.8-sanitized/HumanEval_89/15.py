def encrypt(string):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate_by = 2 * 2

    for char in string:
        index = alphabet.find(char)
        new_index = (index + rotate_by) % len(alphabet)
        encrypted += alphabet[new_index]
    return encrypted