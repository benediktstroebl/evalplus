def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    new_message = ''
    
    for char in message:
        if char.isalpha():
            index = alphabet.find(char)
            new_index = (index + 1) if char in vowels else index + 2
            new_message += alphabet[new_index]
        else:
            new_message += char
            
    return new_message