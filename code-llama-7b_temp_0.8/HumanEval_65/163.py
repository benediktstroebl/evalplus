
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
    x_str_len = len(x_str)

    if shift > x_str_len:
        x_str_len = x_str_len - 1
        return x_str[x_str_len] + x_str[:x_str_len]

    return x_str[shift:] + x_str[:shift]

