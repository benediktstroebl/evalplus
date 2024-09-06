
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    shifted_str = str_x[shift:] + str_x[:shift]
    if len(str_x) == len(shifted_str):
        return shifted_str
    else:
        return shifted_str[::-1]
