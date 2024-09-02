
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # assert 0 <= shift <= len(x), "Shift must be in range."
    # assert x >= 0, "Number must be non-negative."
    if shift == 0:
        return x
    elif shift >= len(x):
        return x[-1] * len(x) + x[:-1]
    else:
        return x[shift:] + x[:shift]

