def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''

    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded += alphabet[alphabet.find(char) + 2]
            else:
                encoded += char.swapcase()
        else:
            encoded += char

    return encoded