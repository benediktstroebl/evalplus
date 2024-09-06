
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    new_x = str(x)
    if len(new_x) > shift:
        return new_x[shift:] + new_x[:shift]
    else:
        return new_x[-shift:] + new_x[:-shift
