
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 0:
        x = str(-x)
    else:
        x = str(x)
    x = x[-shift:] + x[:-shift]
    return x[::-1] if shift > len(x) else x

