def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() if letter.isalpha() else letter for letter in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))