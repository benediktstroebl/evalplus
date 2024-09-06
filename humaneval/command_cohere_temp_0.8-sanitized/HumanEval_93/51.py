def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr((97 + ord(char) - ord(vowels[vowels.find(char)]) + 2) % 26 + 97)
            else:
                new_message += char
        else:
            new_message += char
    return new_message