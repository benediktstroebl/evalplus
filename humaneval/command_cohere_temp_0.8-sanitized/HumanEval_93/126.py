def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    swapped = message.swapcase()
    translated = swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
    
    return translated