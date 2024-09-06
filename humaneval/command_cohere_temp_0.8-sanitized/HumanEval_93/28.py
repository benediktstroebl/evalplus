def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_char = alphabet[alphabet.index(char) + 2]
            else:
                new_char = chr(97 + (ord(char) - 97) ^ 1)
        else:
            new_char = char
        new_message.append(new_char)
    
    return ''.join(new_message)