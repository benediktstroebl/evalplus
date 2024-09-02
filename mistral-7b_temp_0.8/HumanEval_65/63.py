
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    return ''.join([str(x % 10) for x in x // 10 * 10 + x % 10][::-1][shift:] +
                   [str(x % 10) for x in x // 10 * 10 + x % 10][:shift])
