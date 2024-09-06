def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_alphabet = ''.join(alphabet[i::2] for i in range(26))
    
    for char in string:
        if char.isalpha():
            char_code = alphabet.find(char)
            encrypted_code = encoded_alphabet[char_code::2]
            encrypted += encrypted_code
        else:
            encrypted += char
    
    return encrypted