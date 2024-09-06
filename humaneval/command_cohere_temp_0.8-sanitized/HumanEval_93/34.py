def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    new_message = ''
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += alphabet[alphabet.index(char) + 2]
            else:
                new_message += chr(97 + alphabet.index(char))
        else:
            new_message += char
    
    return new_message