
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    length = 0
    x = str(x)
    while x[length:] != "":
        length += 1
    if length > shift:
        x = x[length - shift :] + x[0 : length - shift]
    else:
        x = x[length - shift :] + x[0 : length - shift]
    return x

