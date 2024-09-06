def circular_shift(x, shift):
    digits = str(x)
    result = digits[shift:] + digits[:shift]
    if len(result) < len(digits):
        return result
    else:
        return result[::-1]