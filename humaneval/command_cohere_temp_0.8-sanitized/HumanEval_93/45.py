def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []

    for char in message:
        if char.isalpha():
            if char in vowels:
                new_char = alphabet[alphabet.index(char) + 2]
            else:
                new_char = char.swapcase()
            new_message.append(new_char)
        else:
            new_message.append(char)

    return ''.join(new_message)