def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() for letter in message if letter.isalpha())
    encoded = ''.join(char if char not in vowels else vowels.find(char) + 2 for char in message)
    return swapped + encoded