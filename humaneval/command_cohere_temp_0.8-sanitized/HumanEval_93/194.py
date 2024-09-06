def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))