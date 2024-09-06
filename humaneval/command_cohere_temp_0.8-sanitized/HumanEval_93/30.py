def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                offset = ord('a') if char in 'aeiou' else ord('A')
                new_message.append(alphabet[offset + 2 + (ord(char) - offset) % 26])
            else:
                new_message.append(char.swapcase())
        else:
            new_message.append(char)
    
    return ''.join(new_message)