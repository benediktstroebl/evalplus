
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # make sure shift is within the range of the number of digits in x
    shift %= len(str(x))
    if shift == 0:
        return str(x)
    else:
        return str(x)[:-shift]
