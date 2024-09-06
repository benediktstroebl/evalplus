def circular_shift(x, shift):
    s = str(x)
    digit_len = len(s)
    if shift > digit_len:
        shift = digit_len
    return s[shift:] + s[:shift]