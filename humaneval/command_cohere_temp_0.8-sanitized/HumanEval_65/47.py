def circular_shift(x, shift):
    digits = str(x)
    result = digits[shift:] + digits[:shift]
    if len(result) > len(digits):
        result = result[::-1]
    return result