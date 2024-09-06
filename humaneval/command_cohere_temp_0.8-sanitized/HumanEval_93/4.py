def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''.join(alphabet[alphabet.index(c) + 2 if c in vowels else 1] if c.isalpha() else c for c in message)
    return res.upper() if res.islower() else res.lower()