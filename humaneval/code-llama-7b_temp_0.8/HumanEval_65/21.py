
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 0:
        raise ValueError("input must be a positive integer")
    str_x = str(x)
    # check to see if shift is larger than number of digits
    if shift > len(str_x):
        shift = len(str_x)
    str_x = str_x[-shift:] + str_x[:-shift]
    return str_x

