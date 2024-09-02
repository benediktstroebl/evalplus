
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if not isinstance(x, int):
        raise TypeError("expected an int")
    if not isinstance(shift, int):
        raise TypeError("expected an int")
    if not x >= 0:
        raise ValueError("expected non-negative")
    if not shift >= 0:
        raise ValueError("expected non-negative")
    if shift > len(str(x)):
        return str(x)[::-1]
    return str(x)[-shift:] + str(x)[:-shift]

