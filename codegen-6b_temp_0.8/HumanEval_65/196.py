
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n_digits = len(str(x))
    if shift > n_digits:
        shift = shift % n_digits
    res = list(str(x))
    res.append(res[:shift])
    return "".join(res[shift:])

