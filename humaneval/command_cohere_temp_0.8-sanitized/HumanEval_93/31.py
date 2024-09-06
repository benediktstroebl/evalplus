def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    res = ''
    for char in message:
        if char.isalpha():
            char_idx = alphabet.find(char)
            new_char_idx = (char_idx + 2) % 26 + alphabet[0]
            new_char = alphabet[new_char_idx]
            res += new_char if new_char in vowels else char
        else:
            res += char
    return res