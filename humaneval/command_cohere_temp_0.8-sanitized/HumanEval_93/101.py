def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.swapcase() if c.isalpha() and c not in vowels else
        vowels.index(c) + 2 + vowels[vowels.index(c) + 1]
        for c in message
    )
    return new_message