def circular_shift(x, shift):
    s = str(x)
    digit_count = len(s)
    if shift > digit_count:
        shift = digit_count
    return s[-shift:] + s[:-shift]