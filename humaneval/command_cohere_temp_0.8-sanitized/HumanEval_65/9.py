def circular_shift(x, shift):
    digits = str(x)
    if shift > len(digits):
        shift = len(digits)
    return digits[shift:] + digits[:shift]