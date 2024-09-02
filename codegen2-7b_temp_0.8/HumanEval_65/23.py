
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if not shift:
        return str(x)
    str_x = str(x)
    if len(str_x) < shift:
        return circular_shift(str_x, shift - len(str_x)) + str_x[shift - 1]
    return str_x[shift:] + str_x[:shift]

