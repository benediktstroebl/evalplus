
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    return a string
    if shift > number of digits, return digits reversed.
    """
    x = str(x)
    l = len(x)
    if l <= 1:
        return x

    if shift > l:
        shift = shift % l
    if shift == 0:
        return x

    # if shift < 0:
    #     shift = abs(shift)
    #     x = x[shift:] + x[:shift]

    return x[shift:] + x[:shift]

