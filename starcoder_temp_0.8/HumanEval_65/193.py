
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
    x_len = len(x_str)
    if shift > x_len:
        shift = shift % x_len
        if shift == 0:
            return x_str[::-1]
        else:
            return x_str[-shift:][::-1] + x_str[:-shift]
    return x_str[x_len - shift:] + x_str[:x_len - shift]
