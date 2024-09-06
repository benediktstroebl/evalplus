def circular_shift(x, shift):
    s = str(x)
    digits = list(s)
    if shift > len(s):
        shift = len(s)
    digits = digits[-shift:] + digits[:-shift]
    return ''.join(digits)