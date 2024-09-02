
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert to string, cast shift to int
    x = str(x)
    shift = int(shift)
    # number of digits
    num_dig = len(x)
    # if shift is larger than number of digits, return digits reversed
    if shift > num_dig:
        return x[::-1]
    else:
        # otherwise, return digits shifted
        return x[-shift:] + x[:-shift]

