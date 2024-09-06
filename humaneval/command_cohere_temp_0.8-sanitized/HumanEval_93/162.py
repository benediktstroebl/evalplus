def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(char.swapcase() if char.isalpha() else char for char in message)
    return swapped.lower() if char.lower() not in vowels else swapped.lower()[:2]+chr(ord(swapped.lower()[:2])+2)*(' '*swapped.lower()[2:])