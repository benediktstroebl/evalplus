
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x, shift = str(x), shift
    if not x:
        return ''
    if shift <= len(x):
        return x[shift:] + x[:shift]
    else:
        return x[len(x) - (shift - len(x)) :] + x[: len(x) - (shift - len(x))]
