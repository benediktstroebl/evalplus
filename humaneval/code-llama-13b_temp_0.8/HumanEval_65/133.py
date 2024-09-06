
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if len(s) >= shift:
        # zero pad on left to keep digits to right of shift
        return (s + "0" * shift)[-shift:]
    else:
        return s[::-1]

