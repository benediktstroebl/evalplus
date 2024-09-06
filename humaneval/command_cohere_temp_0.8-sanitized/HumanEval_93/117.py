def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() for letter in message if letter.isalpha())
    translated = swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
    return translated