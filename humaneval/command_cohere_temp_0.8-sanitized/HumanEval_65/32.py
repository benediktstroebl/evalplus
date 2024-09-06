def circular_shift(x, shift):
    digits = str(x)
    if len(digits) < shift:
        return digits[len(digits) % shift:] + digits[: len(digits) % shift]
    return digits[shift:] + digits[:shift]