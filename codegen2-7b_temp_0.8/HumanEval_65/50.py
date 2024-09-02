
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
    if len(y) == 1:
        return "0" + y
    elif len(y) == 2:
        return y[1] + y[0]
    elif len(y) > 2:
        return y[shift:] + y[:shift]
    else:
        return "0
