
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_string = str(x)
    x_len = len(x_string)
    if x_len <= shift:
        return x_string[::-1]

    new_string = x_string[shift:] + x_string[:shift]

    return new_string

