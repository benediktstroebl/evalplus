def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.lower() in vowels) + 96)
            else:
                new_message += chr(96 + char.lower())
        else:
            new_message += char
    return new_message