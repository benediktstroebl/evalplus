
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = str(x)
    while shift > len(x):
        shift -= len(x)

    if shift == 0:
        return x

    if shift < 0:
        return x[-shift:] + x[:shift]

    if shift == len(x):
        return x[::-1]

    if shift < len(x):
        return x[shift:] + x[:shift]

    return x[-shift:] + x[:shift]
