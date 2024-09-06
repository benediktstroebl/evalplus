def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''.join(
        alphabet[alphabet.find(c) + (alphabet.find(c) + 2) % 26]
        if c in vowels
        else c
        for c in message
    )
    return res.swapcase()