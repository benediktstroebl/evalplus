
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    x_str = str(x)
    if shift <= len(x_str):
        return int(x_str[-shift:] + x_str[:-shift])
    else:
        return int(x_str[:len(x_str)-shift] + x_str[len(x_str)-shift:])
