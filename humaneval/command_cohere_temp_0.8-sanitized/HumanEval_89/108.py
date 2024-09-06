def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rot_index_map = {alphabet[i]: alphabet[i+2*s.count(alphabet[i])] 
                      for i in range(26)}
    for ch in s:
        encrypted += rot_index_map[ch]
    return encrypted