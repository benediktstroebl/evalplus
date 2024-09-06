
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
    str_x = str_x[::-1]
    i = 0
    while i < shift:
        str_x = str_x[1:] + str_x[0]
        i += 1
    return int(str_x)
