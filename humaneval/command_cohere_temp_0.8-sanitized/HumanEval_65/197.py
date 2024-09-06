def circular_shift(x, shift):
    s = str(x)
    return s[-shift:] + s[:-shift] if shift < len(s) else s[len(s) - shift:] + s[:len(s) - shift]