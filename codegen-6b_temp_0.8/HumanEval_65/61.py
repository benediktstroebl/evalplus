
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    c_sh = shift % len(str(x))
    if c_sh == 0:
        return str(x)
    else:
        return str(x)[-c_sh:] + str(x)[:-c_sh]

