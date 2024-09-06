def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.swapcase() if c.isalpha() and c not in vowels else
        vowels.index(c) + 2 for c in message if c.isalpha()
    )
    return new_message