
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
    l = len(x_str)
    if l == 0:
        return x_str
    elif l == 1:
        return str(x % 10)
    return x_str[shift % l :] + x_str[: shift % l
