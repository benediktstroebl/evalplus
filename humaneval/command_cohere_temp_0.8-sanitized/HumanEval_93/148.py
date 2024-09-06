def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() and c not in vowels else vowels.index(c) + 2 for c in message)
    return swapped