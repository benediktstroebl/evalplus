def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]