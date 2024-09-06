def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:]+digits[:-shift] if len(digits) >= shift else digits[::-1]