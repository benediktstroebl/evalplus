def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.upper() != char) + 96 + (ord(char) - 96 + 2) if char in vowels[:-1] else 97 + (ord(char) - 97 + 2))
            else:
                new_message += chr((char.upper() != char) + 96 + ord(char))
        else:
            new_message += char
    return new_message