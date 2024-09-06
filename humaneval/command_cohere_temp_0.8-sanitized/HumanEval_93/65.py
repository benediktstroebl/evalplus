def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((char.upper() - 65) + (ord(vowels[vowels.index(char)] - 64)) )
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message