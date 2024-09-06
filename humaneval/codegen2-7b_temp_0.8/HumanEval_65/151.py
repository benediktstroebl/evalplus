
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    mask = 10 ** len(str(x)) - 1
    x = str(x)
    shifted = x[shift:] + x[:shift]
    return (shifted[:len(x)] + mask * shifted[len(x):]).lstrip('0')
