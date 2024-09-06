def circular_shift(x, shift):
    s = str(x)
    digits = len(s)
    if shift > digits:
        shift = shift % digits
    return s[shift:] + s[:shift]