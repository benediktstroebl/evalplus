def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''.join(alphabet[alphabet.index(c) + (c in vowels) * 2] for c in message if c in alphabet)
    return encoded