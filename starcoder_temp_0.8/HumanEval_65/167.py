
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
    str_shift = str(shift)
    if len(str_shift) < len(str_x):
        return str_x[len(str_x)-int(str_shift):]+str_x[:len(str_x)-int(str_shift)]
    else:
        return str_x[::-1]
