def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                res += alphabet[alphabet.index(char) + 2]
            else:
                res += char.swapcase()
        else:
            res += char
    return res