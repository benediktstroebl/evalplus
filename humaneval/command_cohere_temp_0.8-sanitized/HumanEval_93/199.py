def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''.join(alphabet[alphabet.index(c) + (c in vowels and 2 or 0)] for c in message)
    return encoded