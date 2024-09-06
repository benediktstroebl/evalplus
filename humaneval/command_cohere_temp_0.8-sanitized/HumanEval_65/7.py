def circular_shift(x, shift):
    s = str(x)
    digit_count = len(s)
    if shift > digit_count:
        return s[::-1]
    return s[-shift:] + s[:-shift]