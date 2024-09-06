def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_message += chr((char.lower() in vowels)-2 + 96)
            else:
                new_message += chr(96 + (ord(char.lower()) - 96) % 26)
        else:
            new_message += char
    return new_message