def circular_shift(x, shift):
    s = str(x)
    digits = list(s)
    if shift > len(s):
        shift = shift % len(s)  # cap shift at number of digits
    digits = digits[shift:] + digits[:shift]
    return ''.join(digits)