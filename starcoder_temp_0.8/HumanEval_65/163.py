
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    num_str = str(x)
    if shift > len(num_str):
        num_str = num_str[::-1]
    else:
        num_str = num_str[-shift:] + num_str[:-shift]
    return num_str
