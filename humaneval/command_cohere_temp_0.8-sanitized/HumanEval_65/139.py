def circular_shift(x, shift):
    s = str(x)
    digits = list(s)
    if shift > len(s):
        shift = shift % len(s)  # this handles the case where shift > number of digits and shifts any number left/right equally
    digits = digits[-shift:] + digits[:-shift]
    return ''.join(digits)