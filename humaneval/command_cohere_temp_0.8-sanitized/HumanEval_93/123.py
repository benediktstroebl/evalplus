def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                res += alphabet[alphabet.find(char) + 2]
            else:
                res += alphabet[alphabet.find(char) + 1]
        else:
            res += char
    return res