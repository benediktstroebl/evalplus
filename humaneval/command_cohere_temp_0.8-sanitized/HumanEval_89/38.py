def encrypt(s):
    encrypted = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot_index_map = {alphabet[i]: alphabet[i + 2 * s.count(alphabet[0])] 
                      for i in range(26)}
    for char in s:
        if char in alphabet:
            encrypted.append(rot_index_map[char])
        else:
            encrypted.append(char)
    return ''.join(encrypted)