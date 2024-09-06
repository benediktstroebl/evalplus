def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() and c not in vowels else (vowels.find(c) + 2) % 26 + chr(vowels.find(c) + 97) for c in message)
    return swapped