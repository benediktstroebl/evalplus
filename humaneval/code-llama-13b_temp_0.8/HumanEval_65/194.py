
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    length = len(str(x))
    shift = shift % length
    if shift != 0:
        s = str(x)[shift:] + str(x)[:shift]
    else:
        s = str(x)
    return s

