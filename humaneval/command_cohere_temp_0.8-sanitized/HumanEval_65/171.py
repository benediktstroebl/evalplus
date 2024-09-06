def circular_shift(x, shift):
    num_digits = len(str(x))
    x = str(x)
    if shift > num_digits:
        shift = num_digits
    return x[shift:] + x[:shift]