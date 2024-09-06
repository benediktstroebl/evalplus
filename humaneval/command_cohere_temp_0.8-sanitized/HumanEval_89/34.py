def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in s:
        index = alphabet.find(char)
        delta = 2*(index+1)
        new_index = (alphabet_length + index - 1) // 2 + delta
        encrypted += alphabet[(new_index)%alphabet_length]

    return encrypted