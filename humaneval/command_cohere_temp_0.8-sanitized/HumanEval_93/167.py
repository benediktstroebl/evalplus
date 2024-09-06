def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.upper() == char) + 96 + (ord(char) - 96 + 2) % 26 + 96)
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message