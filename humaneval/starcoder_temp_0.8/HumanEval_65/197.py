
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    shift = shift % len(str(x))
    y = str(x)
    z = ""
    for i in range(len(y)):
        z += y[(i + shift) % len(y)]
    return z

