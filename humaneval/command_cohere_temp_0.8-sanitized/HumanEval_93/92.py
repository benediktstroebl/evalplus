def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((ord(char) - 96) + (ord(vowels[vowels.index(char) + 2]) - 96))
            else:
                new_message += chr(ord(char) ^ 32)
        else:
            new_message += char
    return new_message