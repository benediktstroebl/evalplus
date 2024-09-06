
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # The integer to string conversion here is to ensure that the
    # type of the argument is correct, in case someone calls
    # circular_shift with a float or string.
    s = str(x)
    length = len(s)
    if shift > length:
        return s[::-1]
    else:
        return s[length - shift:] + s[:length - shift]
