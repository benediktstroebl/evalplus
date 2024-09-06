
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    y = str(x)
    if y[0] == '0' and len(y) > 1:
        y = y[1:]
    x = str(x)
    if len(x) < shift:
        return y + x
    else:
        return y[shift:] + x[:shift]

