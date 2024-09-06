
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
    if shift > len(y):
        return y[::-1]
    elif shift < 0:
        return y[(-1 * shift):] + y[0:(len(y) - shift)]
    else:
        return y[shift:] + y[:shift]

