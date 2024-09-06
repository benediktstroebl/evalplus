def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_index_map = {alphabet[i]: alphabet[i + 2 * 2] for i in range(26)}
    for char in string:
        encrypted += rot_index_map[char]
    return encrypted