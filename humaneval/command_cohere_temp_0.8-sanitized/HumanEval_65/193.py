def circular_shift(x, shift):
    s = str(x)
    return s[-shift:] + s[:-shift] if len(s) < shift else s[shift:] + s[:shift]