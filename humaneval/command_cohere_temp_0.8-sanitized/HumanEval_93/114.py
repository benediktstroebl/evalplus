def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message.append(alphabet[alphabet.find(char) + 2])
            else:
                new_message.append(char.swapcase())
        else:
            new_message.append(char)
    
    return ''.join(new_message)