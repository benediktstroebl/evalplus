
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x >= 0:
        digits = str(x)
        if shift > len(digits):
            digits = digits[::-1]
            shift = shift - len(digits)
        shifted = digits[shift:] + digits[0:shift]
        return "".join(shifted)
    else:
        digits = str(x)[1:]
        if shift > len(digits):
            digits = digits[::-1]
            shift = shift - len(digits)
        shifted = "-" + digits[shift:] + digits[0:shift]
        return "".join(shifted)

