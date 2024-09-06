def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotation = 2
    for char in string:
        index = alphabet.find(char)
        next_index = (index + rotation) % len(alphabet)
        encrypted += alphabet[next_index]
    return encrypted