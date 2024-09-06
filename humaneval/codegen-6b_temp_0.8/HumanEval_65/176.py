
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    remainder = shift % len(str(x))
    x_str = str(x)
    res = x_str[-remainder:] + x_str[:-remainder]
    if len(res) < len(x_str):
        return res
    else:
        return res[:len(x_str)]

