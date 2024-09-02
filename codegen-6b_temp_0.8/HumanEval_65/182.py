
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert x >= 0
    x_str = str(x)
    shifted = x_str[shift:] + x_str[:shift]
    if len(shifted) > len(x_str):
        return shifted[1:]
    else:
        return shifted

