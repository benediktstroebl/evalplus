def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''.join(
        c.upper() if c.isalpha() and c not in vowels else
        vowels.index(c) + 2 for c in message)
    return new_message