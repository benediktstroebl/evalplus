def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotate_amount = 2 * 2
    for char in s:
        if char.isalpha():
            char_code = alphabet.find(char)
            encrypted_char_code = (char_code + rotate_amount) % len(alphabet)
            encrypted += alphabet[encrypted_char_code]
        else:
            encrypted += char
    return encrypted