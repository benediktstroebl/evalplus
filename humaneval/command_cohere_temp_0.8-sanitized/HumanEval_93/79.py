def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(letter.swapcase() for letter in message if letter.isalpha())
    encoded = ''.join(vowels.index(char) + (26 if char in vowels else 1) for char in swapped)
    return encoded